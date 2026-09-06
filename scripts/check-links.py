#!/usr/bin/env python3
"""Check that every internal link in the docs actually goes somewhere.

Two things go wrong often enough to be worth catching automatically:

  - a link to a file that has been renamed or does not exist yet
  - a link to a `#heading` anchor that has been reworded, so the link
    still works but silently drops the reader at the top of the page

Both are invisible when you write them and annoying when you hit one,
which is exactly the kind of thing a machine should be checking.

    python3 scripts/check-links.py

External links are skipped by default: this runs in CI, and a link
checker that hits the network is a link checker that fails for reasons
that have nothing to do with the change.

    python3 scripts/check-links.py --external

checks them anyway. Run it by hand every so often, not in CI. A link to
somebody else's site can rot without anybody touching this repo, and a
dead link in a guide sends a beginner somewhere that tells them they
are lost.
"""

import glob
import os
import re
import sys

# [text](target) — but not ![image](target), which is handled the same way
# anyway since a missing image path is also worth knowing about.
LINK = re.compile(r"(?<!\])\[[^\]]*\]\(([^)\s]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.*?)\s*$", re.M)
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
# `[words](address)` inside backticks is a worked example of link syntax,
# not a link. Same for anything in a fenced block. Strip both before looking.
INLINE_CODE = re.compile(r"(`+)(?:.|\n)*?\1")
SKIP = ("http://", "https://", "mailto:", "#!")


def prose_lines(text):
    """Yield (lineno, line) for lines outside fenced code blocks, with any
    inline code spans blanked out."""
    fence = None
    for lineno, line in enumerate(text.split("\n"), 1):
        marker = FENCE.match(line)
        if fence is None and marker:
            fence = marker.group(1)[0] * len(marker.group(1))
            continue
        if fence is not None:
            if marker and marker.group(1).startswith(fence[0]) and len(marker.group(1)) >= len(fence):
                fence = None
            continue
        yield lineno, INLINE_CODE.sub("", line)


def slug(heading):
    """Turn a heading into the anchor GitHub generates for it."""
    text = heading.strip().replace("`", "")
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # links inside headings
    text = re.sub(r"[*_]", "", text)                       # bold / italic markers
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"\s+", "-", text.strip()).lower()


def anchors(path):
    text = open(path, encoding="utf-8", newline="").read().replace("\r\n", "\n")
    seen, out = {}, set()
    for heading in HEADING.findall(text):
        base = slug(heading)
        # GitHub appends -1, -2 ... to repeated headings.
        count = seen.get(base, 0)
        out.add(base if not count else f"{base}-{count}")
        seen[base] = count + 1
    return out


def check_external(found):
    """HEAD each external URL once and report anything that is not OK."""
    import urllib.error
    import urllib.request

    problems, unverified, seen = [], [], {}
    for url, where in sorted(found.items()):
        request = urllib.request.Request(url, method="HEAD", headers={
            # Some sites answer a bare urllib request with 403.
            "User-Agent": "Mozilla/5.0 (link check; codetopia onboarding docs)"
        })
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                code = response.status
        except urllib.error.HTTPError as err:
            code = err.code
        except Exception as err:                      # DNS, TLS, timeout
            code = type(err).__name__
        seen[url] = code
        # 403 and friends usually mean the site blocks automated requests,
        # not that the page is missing. Reporting those as broken would
        # teach people to ignore this check, so they are listed apart.
        if code in (403, 405, 429) or not isinstance(code, int):
            unverified.append(f"{code}  {url}")
        elif not (200 <= code < 400):
            for path, lineno in where:
                problems.append(f"{path}:{lineno}: {code}  {url}")

    print(f"Checked {len(seen)} external link(s).")
    if unverified:
        print(f"\n{len(unverified)} could not be checked from here. Open these"
              f" in a browser if you want to be sure:")
        for line in unverified:
            print(f"  {line}")
    return problems


def main():
    external = "--external" in sys.argv
    files = sorted(set(glob.glob("*.md") + glob.glob("**/*.md", recursive=True)))
    cache, problems, found = {}, [], {}

    for path in files:
        text = open(path, encoding="utf-8", newline="").read().replace("\r\n", "\n")
        for lineno, line in prose_lines(text):
            # House style writes external links as <a href="..." target="_blank">,
            # so collect those as well as Markdown ones.
            for url in re.findall(r'<a\s+href="(https?://[^"]+)"', line):
                found.setdefault(url, []).append((path, lineno))
            for target in LINK.findall(line):
                if target.startswith(SKIP):
                    if external and target.startswith(("http://", "https://")):
                        found.setdefault(target, []).append((path, lineno))
                    continue

                relpath, _, anchor = target.partition("#")
                resolved = path if not relpath else os.path.normpath(
                    os.path.join(os.path.dirname(path), relpath)
                )

                if not os.path.exists(resolved):
                    problems.append(f"{path}:{lineno}: no such file: {target}")
                    continue

                if anchor and resolved.endswith(".md"):
                    if resolved not in cache:
                        cache[resolved] = anchors(resolved)
                    if anchor.lower() not in cache[resolved]:
                        problems.append(
                            f"{path}:{lineno}: {os.path.basename(resolved)} "
                            f"has no heading '#{anchor}'"
                        )

    if external:
        problems += check_external(found)

    if problems:
        print(f"\nFound {len(problems)} broken link(s):\n")
        for problem in problems:
            print(f"  {problem}")
        print("\nFix the link, or the heading it points at, and run again.")
        return 1

    print(f"All internal links resolve across {len(files)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
