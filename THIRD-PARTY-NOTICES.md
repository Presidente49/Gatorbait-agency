# Third-party notices

Material in this repo adapted from the projects below is used under each
project's license (MIT or Apache-2.0, as listed). Each upstream `LICENSE` file
was read before integration. Only concepts, runbooks and short paraphrases are
adapted — no upstream code is vendored. Excluded on license grounds:
jub0t/Concat and calesthio/OpenMontage (AGPL-3.0), and
mutonby/openshorts — see `agency/studio/clipping/NOT-INTEGRATED.md`.

> **Follow-up:** sources #8–19 in `agency/docs/SOURCES.md` (added 2026-09-27
> by the repo-shopping pass) still need rows here, with their verbatim
> copyright lines read from each upstream LICENSE.

| Upstream | License | Copyright line (verbatim) | Used in |
|---|---|---|---|
| [avioflagos/marketing-agency-skill](https://github.com/avioflagos/marketing-agency-skill) | MIT | Copyright (c) 2026 David Olatunji | Agency structure: `agency/agents/`, `agency/shared/` (adapted, rebuilt as white-label) |
| [charlie947/social-media-skills](https://github.com/charlie947/social-media-skills) | MIT | Copyright (c) 2026 Charlie Hills | `agency/skills-library/` (17 skills + index) |
| [cgallic/visual-factory-kit](https://github.com/cgallic/visual-factory-kit) | MIT | Copyright (c) 2026 Visual Factory Kit contributors | `agency/studio/creative/` (docs; concepts only) |
| [muneebkhan08/capite](https://github.com/muneebkhan08/capite) | MIT | Copyright (c) 2026 Capite Contributors | `agency/studio/captions/` (docs; concepts only) |
| [ronin1770/reel-quick](https://github.com/ronin1770/reel-quick) | MIT | Copyright (c) 2026 ronin1770 | `agency/studio/reels/` (docs; endpoint names) |
| [arifyaman/multistream](https://github.com/arifyaman/multistream) | MIT | Copyright (c) 2026 xlip | `agency/studio/livestream/` (docs; command model) |
| [Anil-matcha/Free-AI-Social-Media-Scheduler](https://github.com/Anil-matcha/Free-AI-Social-Media-Scheduler) | MIT | Copyright (c) 2023 Anil Chandra Naidu Matcha | `agency/cloud/scheduler/` (deploy docs; app not vendored) |
| [anthropics/commerce-agents](https://github.com/anthropics/commerce-agents) | Apache-2.0 | Anthropic, PBC (LICENSE has no copyright line; no NOTICE file) | `agency/merch/MERCH-OPS-RUNBOOK.md` (concepts only) |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Apache-2.0 | Anthropic, PBC (LICENSE has no copyright line; no NOTICE file) | `agency/skills-library/marketing/` campaign-plan, competitive-brief, email-sequence, seo-audit (adapted, modified) |
| [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | MIT (Tencent-authored code/docs only) | Copyright (C) 2025 Tencent. All rights reserved. | `agency/cloud/weknora/`, `agency/skills-library/research/knowledge-base.md` (concepts only) |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | MIT | Copyright (c) 2025 Bytedance Ltd. and/or its affiliates; Copyright (c) 2025-2026 DeerFlow Authors | `agency/cloud/deer-flow/` (concepts only) |
| [thesysdev/openui](https://github.com/thesysdev/openui) | MIT | Copyright (c) 2011-2024 Thesys Inc. | `agency/studio/creative/GENERATIVE-UI-SPECS.md`, `agency/studio/newsletter/` (concepts + component-library structure) |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | MIT | Copyright (c) 2025 Nous Research | `agency/cloud/hermes/`, hygiene section of `agency/cloud/hindsight/AGENCY-MEMORY-MODEL.md` (concepts only) |
| [stablyai/orca](https://github.com/stablyai/orca) | MIT | Copyright (c) 2026 Lovecast Inc. | `agency/cloud/orca/` (concepts only) |
| [browser-use/video-use](https://github.com/browser-use/video-use) | MIT | Copyright (c) 2026 Browser Use | `agency/studio/video-edit/VIDEO-EDIT-RUNBOOK.md` (concepts only) |
| [every-app/open-seo](https://github.com/every-app/open-seo) | MIT | Copyright (c) 2026 Ben Senescu | `agency/skills-library/marketing/keyword-clustering.md`, `link-prospecting.md`, `local-seo.md` (concepts only) |
| [coollabsio/shoutrrr](https://github.com/coollabsio/shoutrrr) | Apache-2.0 | coollabsio (LICENSE has no copyright line; no NOTICE file) | `agency/cloud/shoutrrr/README.md` (concepts only) |
| [darkzOGx/youtube-automation-agent](https://github.com/darkzOGx/youtube-automation-agent) | MIT | Copyright (c) 2025 YouTube Automation Agent Contributors | `agency/growth/PACKAGING-TESTS.md` (concepts only) |

Fonts, logos and photos are separate assets under their own licenses —
record them per brand (see `agency/studio/creative/BRAND-PACK.md`).

## MIT License (applies to each project above, with its copyright line)

```
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

**Tencent/WeKnora note:** WeKnora's LICENSE is MIT "except for the third-party
components listed" (Apache-2.0, BSD, MIT, MPL-2.0, CC-BY-4.0, Python-2.0, and
entries marked "nolicense"/"unknown"). None of those components — code, data or
text — was copied or adapted; only Tencent-authored design patterns were
re-expressed in our own words.

## Apache License 2.0 (applies to the Apache-2.0 projects above)

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
these adapted files except in compliance with the License. You may obtain a copy
of the License at https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

Files adapted from Apache-2.0 projects are marked as modified by their
attribution header ("Adapted for Gator Bait Agency"). Neither upstream ships a
NOTICE file.

