from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "catalog.json"
README_PATH = ROOT / "README.md"
STATUS_ICON_MAP = {
    "Obtainable": "assets/status/yes.svg",
    "Retired": "assets/status/no.svg",
    "Unreleased / undocumented": "assets/status/unknown.svg",
}
EARN_ICON_MAP = {
    "Yes": "assets/status/yes.svg",
    "No": "assets/status/no.svg",
    "Unknown": "assets/status/unknown.svg",
}


def load_catalog() -> dict:
    return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))


def markdown_table(rows: list[list[str]]) -> str:
    headers = rows[0]
    separators = ["---"] * len(headers)
    parts = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(separators) + " |",
    ]
    for row in rows[1:]:
        parts.append("| " + " | ".join(row) + " |")
    return "\n".join(parts)


def render_icon(path: str, alt: str, width: int = 24) -> str:
    return f'<img src="{path}" alt="{alt}" width="{width}">'


def render_status(path: str, label: str) -> str:
    return f'{render_icon(path, label, width=16)} {label}'


def render_badge(path: str, alt: str) -> str:
    return render_icon(path, alt, width=44)


def build_section(title: str, items: list[dict]) -> str:
    rows = [[
        "Name",
        "Type",
        "Status",
        "Earn now?",
        "How to get / known criteria",
        "Notes",
        "Refs",
    ]]

    for item in items:
        status_label = item["status"]
        earn_label = item["can_earn_now"]
        status_icon = STATUS_ICON_MAP.get(status_label, STATUS_ICON_MAP["Unreleased / undocumented"])
        earn_icon = EARN_ICON_MAP.get(earn_label, EARN_ICON_MAP["Unknown"])
        rows.append([
            f'{render_badge(item["image"], item["name"])}<br><strong>{item["name"]}</strong>',
            item["type"],
            render_status(status_icon, status_label),
            render_status(earn_icon, earn_label),
            item["how"],
            item["notes"],
            ", ".join(item["refs"]),
        ])

    return f"## {title}\n\n{markdown_table(rows)}\n"


def build_readme(catalog: dict) -> str:
    items = catalog["items"]
    status_counts = Counter(item["status"] for item in items)
    confidence_counts = Counter(item["source_confidence"] for item in items)

    official = [item for item in items if item["source_confidence"] == "Official"]
    mixed = [item for item in items if item["source_confidence"] == "Mixed"]
    community = [item for item in items if item["source_confidence"] == "Community"]

    sections = [
        f"# {catalog['repo_name']}",
        "",
        "Track GitHub profile badges and achievements, including which ones are still earnable, which ones are retired, and which ones are only community-reported.",
        "",
        f"Last verified: **{catalog['snapshot_date']}**",
        "",
        "## Scope",
        "",
        "- This repo focuses on profile-visible GitHub badges and achievements.",
        "- It separates **officially documented** items from **mixed** and **community-reported** items.",
        "- GitHub does **not** publish a complete official achievements catalog, so some rows are marked with lower confidence on purpose.",
        "- Community rows are useful, but you should treat them as best-effort guidance rather than guaranteed GitHub policy.",
        "",
        "## Snapshot",
        "",
        f"- Total tracked items: **{len(items)}**",
        f"- Obtainable: **{status_counts.get('Obtainable', 0)}**",
        f"- Retired: **{status_counts.get('Retired', 0)}**",
        f"- Unreleased / undocumented: **{status_counts.get('Unreleased / undocumented', 0)}**",
        f"- Official rows: **{confidence_counts.get('Official', 0)}**",
        f"- Mixed-confidence rows: **{confidence_counts.get('Mixed', 0)}**",
        f"- Community rows: **{confidence_counts.get('Community', 0)}**",
        "",
        "## Confidence Legend",
        "",
        "- **Official**: backed directly by GitHub Docs, GitHub Blog, GitHub Changelog, or GitHub-owned program pages.",
        "- **Mixed**: GitHub officially shows the name or concept, but the detailed unlock rule is community-maintained.",
        "- **Community**: widely reported in the GitHub community, but not formally documented by GitHub.",
        "",
        build_section("Officially Documented Items", official),
        build_section("Mixed-Confidence Items", mixed),
        build_section("Community-Reported Items", community),
        "## Notes",
        "",
        "- Program badges such as **PRO** or **Developer Program Member** may disappear if the underlying subscription or membership ends.",
        "- Historical event badges such as **Arctic Code Vault Contributor** and **Mars 2020 Helicopter Contributor** are retired.",
        "- GitHub achievements are still described by GitHub as a **public preview** feature and may change over time.",
        "- Private contributions and achievements can be shown or hidden from profile settings.",
        "",
        "## General Counting Rules That Often Matter",
        "",
        "- Commits usually count only when they use an email address associated with your GitHub account.",
        "- Commits usually need to land on the repository's default branch or on `gh-pages`.",
        "- Commits made only in a fork do not normally count as profile contributions until they are merged where GitHub counts them.",
        "- Issues, pull requests, and discussions count on standalone repositories, not inside forks.",
        "- Private activity only affects achievements if you enable private contributions and achievements in profile settings.",
        "- GitHub may take time to show new achievements, so immediate unlocks are not guaranteed.",
        "",
        "## Sources",
        "",
        "- `D1`: GitHub Docs, Profile reference - https://docs.github.com/en/account-and-profile/reference/profile-reference",
        "- `D2`: GitHub Docs, Profile contributions reference - https://docs.github.com/en/account-and-profile/reference/profile-contributions-reference",
        "- `D3`: GitHub Docs, Manage visibility settings for private contributions and achievements - https://docs.github.com/en/account-and-profile/how-tos/contribution-settings/manage-visibility-settings-for-private-contributions-and-achievements",
        "- `B1`: GitHub Blog, Introducing Achievements - https://github.blog/news-insights/product-news/introducing-achievements-recognizing-the-many-stages-of-a-developers-coding-journey/",
        "- `B2`: GitHub Changelog, Achievements public beta - https://github.blog/changelog/2022-06-09-achievements-public-beta/",
        "- `B3`: GitHub Blog, Open source goes to Mars - https://github.blog/news-insights/company-news/open-source-goes-to-mars/",
        "- `B4`: GitHub Archive Program, Arctic Vault - https://archiveprogram.github.com/arctic-vault/",
        "- `C1`: GitHub Community discussion #176080 (community-maintained) - https://github.com/orgs/community/discussions/176080",
        "",
        "## Updating",
        "",
        "If you update `data/catalog.json`, regenerate this README with:",
        "",
        "```bash",
        "python scripts/render_readme.py",
        "```",
    ]

    return "\n".join(sections).rstrip() + "\n"


def main() -> None:
    catalog = load_catalog()
    README_PATH.write_text(build_readme(catalog), encoding="utf-8")


if __name__ == "__main__":
    main()
