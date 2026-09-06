# Graph Report - portofolio-maheza-novrayuda  (2026-09-06)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 1807 nodes · 2874 edges · 276 communities (52 shown, 40 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 140 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0a538823`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- jquery.min.js
- jquery.min.2c872dbe60f4.js
- Transformation
- Transformation
- xregexp.js
- xregexp.a7e08b0ce686.js
- jquery.cloudinary.js
- jquery.js
- jquery.12e87d2f3a4c.js
- TextLayer
- SelectAdapter
- SelectAdapter
- jquery.cloudinary.171ee44fcb5e.js
- Cloudinary
- Cloudinary
- select2.full.js
- select2.full.c2afdeda3058.js
- xregexp.min.js
- xregexp.min.f1ae4617847c.js
- TextLayer
- HtmlTag
- .append
- .append
- HtmlTag
- .trigger
- .trigger
- .apply
- .apply
- .get
- .get
- package.json
- BaseSelection
- BaseSelection
- Results
- Results
- Expression
- Expression
- views.py
- models.py
- find
- find
- .on
- .on
- select2.full.min.js
- select2.full.min.fcd7500d8e13.js
- ollama
- RelatedObjectLookups.js
- RelatedObjectLookups.ed6240809a40.js
- Animation
- Animation
- Project
- Configuration
- Configuration
- AboutView
- domManip
- domManip
- Profile
- actions.js
- actions.f1d5653edb59.js
- jquery.ui.widget.js
- admin.py
- Skill
- nodeName
- nodeName
- BaseAdapter
- BaseAdapter
- load-image.all.min.js
- load-image.all.min.d0068a911289.js
- vercel.json
- calendar.js
- calendar.d64496bbf46d.js
- theme.js
- theme.91cf832f559e.js
- MaximumSelectionLength
- MaximumSelectionLength
- PortfolioConfig
- main
- initSidebarQuickFilter
- initSidebarQuickFilter
- urlify.js
- urlify.ae970a820212.js
- build_files.sh
- 0001_initial.py
- 0002_contactmessage_profile_about_long_profile_avatar_and_more.py
- 0003_achievement_certificate.py
- 0004_education_rename_twitter_url_profile_instagram_url_and_more.py
- 0005_certificate_file_alter_certificate_image.py
- 0006_alter_certificate_file_alter_project_document_and_more.py
- createCache
- inspectPrefiltersOrTransports
- createCache
- inspectPrefiltersOrTransports

## God Nodes (most connected - your core abstractions)
1. `Transformation()` - 58 edges
2. `Transformation()` - 58 edges
3. `Cloudinary()` - 30 edges
4. `Cloudinary()` - 30 edges
5. `Profile` - 24 edges
6. `TextLayer()` - 21 edges
7. `TextLayer()` - 21 edges
8. `TransformationBase()` - 19 edges
9. `TransformationBase()` - 19 edges
10. `Project` - 18 edges

## Surprising Connections (you probably didn't know these)
- `migrate_media_to_cloudinary()` --uses--> `Project`  [INFERRED]
  migrate_cloudinary.py → portfolio/models.py
- `migrate_media_to_cloudinary()` --uses--> `Profile`  [INFERRED]
  migrate_cloudinary.py → portfolio/models.py
- `setup()` --uses--> `Profile`  [INFERRED]
  scripts/setup_project.py → portfolio/models.py
- `migrate_media_to_cloudinary()` --uses--> `Skill`  [INFERRED]
  migrate_cloudinary.py → portfolio/models.py
- `ContactView` --uses--> `ContactForm`  [INFERRED]
  portfolio/views.py → portfolio/forms.py

## Import Cycles
- None detected.

## Communities (276 total, 40 thin omitted)

### Community 0 - "jquery.min.js"
Cohesion: 0.08
Nodes (36): Ae(), B(), Be(), c(), $e(), ee(), F(), fe() (+28 more)

### Community 1 - "jquery.min.2c872dbe60f4.js"
Cohesion: 0.08
Nodes (36): Ae(), B(), Be(), c(), $e(), ee(), F(), fe() (+28 more)

### Community 4 - "xregexp.js"
Cohesion: 0.07
Nodes (26): _arrayLikeToArray(), augment(), buildAstral(), cacheAstral(), cacheInvertedBmp(), charCode(), clipDuplicates(), copyRegex() (+18 more)

### Community 5 - "xregexp.a7e08b0ce686.js"
Cohesion: 0.07
Nodes (26): _arrayLikeToArray(), augment(), buildAstral(), cacheAstral(), cacheInvertedBmp(), charCode(), clipDuplicates(), copyRegex() (+18 more)

### Community 6 - "jquery.cloudinary.js"
Cohesion: 0.08
Nodes (11): ArrayParam(), ClientHintsMetaTag(), ExpressionParam(), FetchLayer(), LayerParam(), Param(), RangeParam(), RawParam() (+3 more)

### Community 7 - "jquery.js"
Cohesion: 0.07
Nodes (12): computeStyleTests(), dataAttr(), finalPropName(), getData(), Identity(), leverageNative(), NOTE: This can be skipped if there are no unmatched elements (i.e.,…, resolve() (+4 more)

### Community 8 - "jquery.12e87d2f3a4c.js"
Cohesion: 0.07
Nodes (12): computeStyleTests(), dataAttr(), finalPropName(), getData(), Identity(), leverageNative(), resolve(), returnTrue() (+4 more)

### Community 9 - "TextLayer"
Cohesion: 0.07
Nodes (5): FetchLayer(), Layer(), LayerParam(), SubtitlesLayer(), TextLayer()

### Community 10 - "SelectAdapter"
Cohesion: 0.12
Nodes (5): ArrayAdapter(), InputData(), SelectAdapter(), Tags(), Tokenizer()

### Community 11 - "SelectAdapter"
Cohesion: 0.12
Nodes (5): ArrayAdapter(), InputData(), SelectAdapter(), Tags(), Tokenizer()

### Community 12 - "jquery.cloudinary.171ee44fcb5e.js"
Cohesion: 0.09
Nodes (7): ArrayParam(), ExpressionParam(), Param(), RangeParam(), RawParam(), TransformationBase(), TransformationParam()

### Community 13 - "Cloudinary"
Cohesion: 0.14
Nodes (3): Cloudinary(), CloudinaryJQuery(), ImageTag()

### Community 14 - "Cloudinary"
Cohesion: 0.14
Nodes (3): Cloudinary(), CloudinaryJQuery(), ImageTag()

### Community 15 - "select2.full.js"
Cohesion: 0.09
Nodes (14): callDep(), ContainerCSS(), countResults(), DropdownCSS(), handler(), hasProp(), makeNormalize(), makeRelParts() (+6 more)

### Community 16 - "select2.full.c2afdeda3058.js"
Cohesion: 0.09
Nodes (14): callDep(), ContainerCSS(), countResults(), DropdownCSS(), handler(), hasProp(), makeNormalize(), makeRelParts() (+6 more)

### Community 17 - "xregexp.min.js"
Cohesion: 0.10
Nodes (12): _arrayLikeToArray(), augment(), cacheInvertedBmp(), charCode(), clipDuplicates(), copyRegex(), _createForOfIteratorHelper(), isType() (+4 more)

### Community 18 - "xregexp.min.f1ae4617847c.js"
Cohesion: 0.10
Nodes (12): _arrayLikeToArray(), augment(), cacheInvertedBmp(), charCode(), clipDuplicates(), copyRegex(), _createForOfIteratorHelper(), isType() (+4 more)

### Community 21 - ".append"
Cohesion: 0.12
Nodes (4): AttachContainer(), InfiniteScroll(), MultipleSelection(), SingleSelection()

### Community 22 - ".append"
Cohesion: 0.12
Nodes (4): AttachContainer(), InfiniteScroll(), MultipleSelection(), SingleSelection()

### Community 23 - "HtmlTag"
Cohesion: 0.13
Nodes (3): ClientHintsMetaTag(), HtmlTag(), VideoTag()

### Community 26 - ".apply"
Cohesion: 0.11
Nodes (7): DecoratedClass(), Defaults(), Dropdown(), makeRequire(), oldMatcher(), wrappedMatcher(), Translation()

### Community 27 - ".apply"
Cohesion: 0.11
Nodes (7): DecoratedClass(), Defaults(), Dropdown(), makeRequire(), oldMatcher(), wrappedMatcher(), Translation()

### Community 28 - ".get"
Cohesion: 0.11
Nodes (8): AjaxAdapter(), HidePlaceholder(), InitSelection(), MaximumInputLength(), MinimumInputLength(), Options(), Placeholder(), Query()

### Community 29 - ".get"
Cohesion: 0.11
Nodes (8): AjaxAdapter(), HidePlaceholder(), InitSelection(), MaximumInputLength(), MinimumInputLength(), Options(), Placeholder(), Query()

### Community 30 - "package.json"
Cohesion: 0.10
Nodes (20): author, description, devDependencies, autoprefixer, postcss, tailwindcss, @tailwindcss/cli, directories (+12 more)

### Community 37 - "views.py"
Cohesion: 0.18
Nodes (9): DetailView, FormView, ListView, method_decorator, ContactView, HomeView, ProjectDetailView, ProjectListView (+1 more)

### Community 38 - "models.py"
Cohesion: 0.14
Nodes (6): ContactForm, Meta, ContactMessage, ContactFormTest, PortfolioViewsTest, TestCase

### Community 39 - "find"
Cohesion: 0.18
Nodes (17): addCombinator(), assert(), compile(), condense(), createPositionalPseudo(), elementMatcher(), find(), markFunction() (+9 more)

### Community 40 - "find"
Cohesion: 0.18
Nodes (17): addCombinator(), assert(), compile(), condense(), createPositionalPseudo(), elementMatcher(), find(), markFunction() (+9 more)

### Community 41 - ".on"
Cohesion: 0.22
Nodes (3): AttachBody(), CloseOnSelect(), EventRelay()

### Community 42 - ".on"
Cohesion: 0.22
Nodes (3): AttachBody(), CloseOnSelect(), EventRelay()

### Community 43 - "select2.full.min.js"
Cohesion: 0.21
Nodes (13): A(), b(), c(), D(), e(), i(), l(), n() (+5 more)

### Community 44 - "select2.full.min.fcd7500d8e13.js"
Cohesion: 0.21
Nodes (13): A(), b(), c(), D(), e(), i(), l(), n() (+5 more)

### Community 45 - "ollama"
Cohesion: 0.14
Nodes (13): name, name, model, llama3.2:1b, llama3:latest, models, name, npm (+5 more)

### Community 46 - "RelatedObjectLookups.js"
Cohesion: 0.24
Nodes (10): addPopupIndex(), dismissAddRelatedObjectPopup(), dismissChangeRelatedObjectPopup(), dismissDeleteRelatedObjectPopup(), dismissRelatedLookupPopup(), removePopupIndex(), showAdminPopup(), showRelatedObjectLookupPopup() (+2 more)

### Community 47 - "RelatedObjectLookups.ed6240809a40.js"
Cohesion: 0.24
Nodes (10): addPopupIndex(), dismissAddRelatedObjectPopup(), dismissChangeRelatedObjectPopup(), dismissDeleteRelatedObjectPopup(), dismissRelatedLookupPopup(), removePopupIndex(), showAdminPopup(), showRelatedObjectLookupPopup() (+2 more)

### Community 48 - "Animation"
Cohesion: 0.15
Nodes (14): adoptValue(), ajaxConvert(), ajaxHandleResponses(), Animation(), camelCase(), createFxNow(), createTween(), defaultPrefilter() (+6 more)

### Community 49 - "Animation"
Cohesion: 0.15
Nodes (14): adoptValue(), ajaxConvert(), ajaxHandleResponses(), Animation(), camelCase(), createFxNow(), createTween(), defaultPrefilter() (+6 more)

### Community 50 - "Project"
Cohesion: 0.21
Nodes (4): Project, ProjectSitemap, StaticViewSitemap, Sitemap

### Community 53 - "AboutView"
Cohesion: 0.20
Nodes (7): Achievement, Certificate, Education, Kind, Meta, AboutView, TemplateView

### Community 56 - "domManip"
Cohesion: 0.20
Nodes (12): buildFragment(), buildParams(), cloneCopyEvent(), disableScript(), DOMEval(), domManip(), getAll(), isArrayLike() (+4 more)

### Community 57 - "domManip"
Cohesion: 0.20
Nodes (12): buildFragment(), buildParams(), cloneCopyEvent(), disableScript(), DOMEval(), domManip(), getAll(), isArrayLike() (+4 more)

### Community 58 - "Profile"
Cohesion: 0.25
Nodes (5): Profile, ProfileSingletonTest, ProjectSlugTest, TestCase, setup()

### Community 59 - "actions.js"
Cohesion: 0.38
Nodes (8): checker(), clearAcross(), hide(), reset(), show(), showClear(), showQuestion(), updateCounter()

### Community 60 - "actions.f1d5653edb59.js"
Cohesion: 0.38
Nodes (8): checker(), clearAcross(), hide(), reset(), show(), showClear(), showQuestion(), updateCounter()

### Community 62 - "admin.py"
Cohesion: 0.33
Nodes (8): AchievementAdmin, CertificateAdmin, ContactMessageAdmin, EducationAdmin, ProfileAdmin, ProjectAdmin, SkillAdmin, register

### Community 63 - "Skill"
Cohesion: 0.28
Nodes (5): BaseCommand, migrate_media_to_cloudinary(), Command, Category, Skill

### Community 64 - "nodeName"
Cohesion: 0.29
Nodes (7): boxModelAdjustment(), createButtonPseudo(), createInputPseudo(), curCSS(), getWidthOrHeight(), manipulationTarget(), nodeName()

### Community 65 - "nodeName"
Cohesion: 0.29
Nodes (7): boxModelAdjustment(), createButtonPseudo(), createInputPseudo(), curCSS(), getWidthOrHeight(), manipulationTarget(), nodeName()

### Community 72 - "vercel.json"
Cohesion: 0.40
Nodes (4): buildCommand, builds, outputDirectory, rewrites

### Community 75 - "theme.js"
Cohesion: 0.83
Nodes (3): cycleTheme(), initTheme(), setTheme()

### Community 76 - "theme.91cf832f559e.js"
Cohesion: 0.83
Nodes (3): cycleTheme(), initTheme(), setTheme()

## Knowledge Gaps
- **38 isolated node(s):** `Meta`, `Kind`, `Category`, `Migration`, `Migration` (+33 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 760 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **40 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Transformation()` connect `Transformation` to `HtmlTag`, `jquery.cloudinary.js`, `Cloudinary`?**
  _High betweenness centrality (0.006) - this node is a cross-community bridge._
- **Why does `Transformation()` connect `Transformation` to `jquery.cloudinary.171ee44fcb5e.js`, `Cloudinary`, `HtmlTag`?**
  _High betweenness centrality (0.006) - this node is a cross-community bridge._
- **Why does `TextLayer()` connect `TextLayer` to `jquery.cloudinary.js`?**
  _High betweenness centrality (0.004) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `Profile` (e.g. with `migrate_media_to_cloudinary()` and `ProfileAdmin`) actually correct?**
  _`Profile` has 11 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Meta`, `Kind`, `Category` to the rest of the system?**
  _38 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `jquery.min.js` be split into smaller, more focused modules?**
  _Cohesion score 0.07896575821104122 - nodes in this community are weakly interconnected._
- **Should `jquery.min.2c872dbe60f4.js` be split into smaller, more focused modules?**
  _Cohesion score 0.07896575821104122 - nodes in this community are weakly interconnected._