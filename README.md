# GitHub Achievements Catalog

Track GitHub profile badges and achievements, including which ones are still earnable, which ones are retired, and which ones are only community-reported.

Last verified: **2026-04-06**

## Scope

- This repo focuses on profile-visible GitHub badges and achievements.
- It separates **officially documented** items from **mixed** and **community-reported** items.
- GitHub does **not** publish a complete official achievements catalog, so some rows are marked with lower confidence on purpose.
- Community rows are useful, but you should treat them as best-effort guidance rather than guaranteed GitHub policy.

## Snapshot

- Total tracked items: **16**
- Obtainable: **12**
- Retired: **2**
- Unreleased / undocumented: **2**
- Official rows: **9**
- Mixed-confidence rows: **2**
- Community rows: **5**

## Confidence Legend

- **Official**: backed directly by GitHub Docs, GitHub Blog, GitHub Changelog, or GitHub-owned program pages.
- **Mixed**: GitHub officially shows the name or concept, but the detailed unlock rule is community-maintained.
- **Community**: widely reported in the GitHub community, but not formally documented by GitHub.

## Officially Documented Items

| Name | Type | Status | Earn now? | How to get / known criteria | Notes | Refs |
| --- | --- | --- | --- | --- | --- | --- |
| Developer Program Member | Profile badge | Obtainable | Yes | Join the GitHub Developer Program and build an app with the GitHub API. | Shown as a profile badge, not an achievement. The badge depends on active program participation. | D1 |
| PRO | Profile badge | Obtainable | Yes | Use GitHub Pro. | Shown while the account has GitHub Pro. | D1 |
| Security Bug Bounty Hunter | Profile badge | Obtainable | Yes | Help GitHub find security vulnerabilities through the security program. | Not a general-purpose badge; it depends on accepted security work. | D1 |
| GitHub Campus Expert | Profile badge | Obtainable | Yes | Participate in the GitHub Campus Experts program. | Program badge for accepted Campus Experts. | D1 |
| Security advisory credit | Profile badge | Obtainable | Yes | Submit a security advisory accepted into the GitHub Advisory Database. | Shown as a profile badge, not an achievement. | D1 |
| Arctic Code Vault Contributor | Achievement / event badge | Retired | No | Contribute to a repository that made the 2020 Arctic Code Vault snapshot. | Snapshot date was February 2, 2020. This is historical and no longer earnable. | B4, D1 |
| Mars 2020 Helicopter Contributor | Achievement / event badge | Retired | No | Contribute to one of the qualifying repository versions used by NASA Ingenuity. | GitHub says the event has ended and the badge is no longer available. | B3, D1 |
| GitHub Sponsors badge (commonly called Public Sponsor) | Achievement / profile badge | Obtainable | Yes | Sponsor a contributor or project through GitHub Sponsors. | GitHub's docs/blog describe the badge, while the community often calls it Public Sponsor. | B1, B3 |
| Galaxy Brain | Achievement | Obtainable | Yes | Have your reply in GitHub Discussions marked as an accepted / helpful answer. | Officially shown in GitHub's launch blog and explained at a high level, but GitHub does not publish all thresholds. | B1, B2 |

## Mixed-Confidence Items

| Name | Type | Status | Earn now? | How to get / known criteria | Notes | Refs |
| --- | --- | --- | --- | --- | --- | --- |
| Pull Shark | Achievement | Obtainable | Yes | Community consensus: open pull requests that get merged. | The name is shown by GitHub in the 2022 changelog image, but detailed criteria and tiers are not officially documented by GitHub. | B2, C1 |
| YOLO | Achievement | Obtainable | Yes | Community consensus: merge a pull request without code review. | The name is shown by GitHub in the 2022 changelog image, but GitHub does not publish official criteria details. | B2, C1 |

## Community-Reported Items

| Name | Type | Status | Earn now? | How to get / known criteria | Notes | Refs |
| --- | --- | --- | --- | --- | --- | --- |
| Starstruck | Achievement | Obtainable | Yes | Community-maintained guidance: receive stars on a repository you own. | Reported tiers in the community guide: Base 16, Bronze 128, Silver 512, Gold 4096 stars. GitHub does not document this officially. | C1 |
| Quickdraw | Achievement | Obtainable | Yes | Community-maintained guidance: close an issue or pull request within 5 minutes of opening it. | Commonly described as one-time. GitHub does not document this officially. | C1 |
| Pair Extraordinaire | Achievement | Obtainable | Yes | Community-maintained guidance: make co-authored commits on pull requests that get merged. | Reported tiers in the community guide: Base 1, Bronze 10, Silver 24, Gold 48. GitHub does not document this officially. | C1 |
| Heart On Your Sleeve | Achievement | Unreleased / undocumented | Unknown | Unknown. | Mentioned in the community guide as listed but not released. No official GitHub criteria were found. | C1 |
| Open Sourcerer | Achievement | Unreleased / undocumented | Unknown | Unknown. | Mentioned in the community guide as listed but not released. No official GitHub criteria were found. | C1 |

## Notes

- Program badges such as **PRO** or **Developer Program Member** may disappear if the underlying subscription or membership ends.
- Historical event badges such as **Arctic Code Vault Contributor** and **Mars 2020 Helicopter Contributor** are retired.
- GitHub achievements are still described by GitHub as a **public preview** feature and may change over time.
- Private contributions and achievements can be shown or hidden from profile settings.

## General Counting Rules That Often Matter

- Commits usually count only when they use an email address associated with your GitHub account.
- Commits usually need to land on the repository's default branch or on `gh-pages`.
- Commits made only in a fork do not normally count as profile contributions until they are merged where GitHub counts them.
- Issues, pull requests, and discussions count on standalone repositories, not inside forks.
- Private activity only affects achievements if you enable private contributions and achievements in profile settings.
- GitHub may take time to show new achievements, so immediate unlocks are not guaranteed.

## Sources

- `D1`: GitHub Docs, Profile reference - https://docs.github.com/en/account-and-profile/reference/profile-reference
- `D2`: GitHub Docs, Profile contributions reference - https://docs.github.com/en/account-and-profile/reference/profile-contributions-reference
- `D3`: GitHub Docs, Manage visibility settings for private contributions and achievements - https://docs.github.com/en/account-and-profile/how-tos/contribution-settings/manage-visibility-settings-for-private-contributions-and-achievements
- `B1`: GitHub Blog, Introducing Achievements - https://github.blog/news-insights/product-news/introducing-achievements-recognizing-the-many-stages-of-a-developers-coding-journey/
- `B2`: GitHub Changelog, Achievements public beta - https://github.blog/changelog/2022-06-09-achievements-public-beta/
- `B3`: GitHub Blog, Open source goes to Mars - https://github.blog/news-insights/company-news/open-source-goes-to-mars/
- `B4`: GitHub Archive Program, Arctic Vault - https://archiveprogram.github.com/arctic-vault/
- `C1`: GitHub Community discussion #176080 (community-maintained) - https://github.com/orgs/community/discussions/176080

## Updating

If you update `data/catalog.json`, regenerate this README with:

```bash
python scripts/render_readme.py
```
