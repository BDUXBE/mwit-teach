# How to Add Lessons & New Subjects

**Read this before building any new lesson.** Everything here is based on the actual working files in this repo.

---

## Repo & GitHub Pages

- **Remote:** `https://github.com/BDUXBE/mwit-teach`
- **Live site:** `https://bduxbe.github.io/mwit-teach/`
- Branch: `master` — GitHub Pages serves from here directly.

### Push to GitHub (every time you finish)

```bash
cd "D:/mwit/Teach"
git add <files you changed>
git commit -m "Short description of what you did"
git push
```

Changes are live within ~1 minute. Hard-refresh with **Ctrl+Shift+R** to bypass cache.

---

## Folder Structure

```
D:/mwit/Teach/
├── index.html                          ← Homepage (accordion dropdowns)
├── HOW-TO-ADD-LESSONS.md               ← This file
│
├── Math/
│   ├── Sequences and Series/
│   │   ├── assets/
│   │   │   ├── style.css               ← Shared stylesheet for ALL S-lessons
│   │   │   ├── quiz.js                 ← Quiz widget (shared)
│   │   │   └── lang.js                 ← EN/TH toggle (shared)
│   │   └── lessons/
│   │       ├── 0000-finite-sequences-and-partial-sums.html   (S1)
│   │       ├── 0001-infinite-sequences.html                  (S2)
│   │       ├── 0002-infinite-series.html                     (S3)
│   │       └── 0004-convergence-tests.html                   (S6)
│   │
│   └── The Derivative Function/
│       ├── assets/
│       │   ├── style.css               ← Shared stylesheet for ALL D-lessons
│       │   ├── quiz.js
│       │   └── lang.js
│       └── lessons/
│           ├── 0003-related-rates.html      (D1)
│           ├── 0001-lhopitals-rule.html     (D2)
│           └── 0002-function-analysis.html  (D4)
│
├── Physics/
│   └── lessons/
│       ├── style.css                   ← Shared stylesheet for ALL P-lessons
│       ├── quiz.js
│       ├── lang.js
│       ├── 0001-origin-of-special-relativity.html   (P1)
│       ├── 0002-time-dilation-length-contraction.html
│       ├── 0003-lorentz-transformation.html
│       ├── 0004-relativistic-momentum-energy.html
│       ├── 0005-blackbody-radiation.html
│       └── 0006-exam-review.html                    (P6)
│
└── หน้าที่พลเมือง/
    └── lessons/
        ├── style.css
        ├── quiz.js
        ├── 0001-kwamru-phunthan-kotmai.html          (C1)
        ├── 0002-rat-ratthathammanun-kotmai-pokkhrong.html
        ├── 0003-kotmai-aya.html
        └── 0004-kotmai-phaeng-bukhkhon.html          (C4)
```

---

## Lesson Filename Convention

```
NNNN-dash-case-title.html
```

- `NNNN` = 4-digit zero-padded number (0001, 0002, …). This is just for ordering files — it does **not** have to match the course lesson number (e.g. file `0003` can be course lesson `D1`).
- Dash-case title describes the content.
- The **course label** (S1, D2, P3, C1…) is shown in the HTML and homepage card only — not in the filename.

---

## There Are Three Lesson Types

| Type | Example subject | Language system | stylesheet path from lesson |
|------|-----------------|-----------------|-----------------------------|
| **Math** | Math/Sequences and Series | `.lang-en` / `.lang-th` divs toggled by `lang.js` | `../assets/style.css` |
| **Physics** | Physics | `data-i18n` attributes + `lang.js` | `style.css` (same folder) |
| **Civic / simple** | หน้าที่พลเมือง | Thai only, no toggle | `style.css` (same folder) |

Use the Math template for any new bilingual math subject. Use Civic template for Thai-only subjects.

---

## Home Button Path — Critical

The home button `← Home` must point to `index.html` at the repo root. The path depends on how deep the lesson file is:

| Lesson depth | Correct href |
|---|---|
| `SubjectFolder/lessons/file.html` (2 folders deep) | `../../index.html` |
| `SubjectFolder/ChapterFolder/lessons/file.html` (3 folders deep) | `../../../index.html` |

**Math lessons are 3 levels deep** → `../../../index.html`  
**Physics and Civic lessons are 2 levels deep** → `../../index.html`

---

## Template: Math Lesson (bilingual EN/TH)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>LESSON TITLE HERE</title>
  <link rel="stylesheet" href="../assets/style.css" />
  <script src="../assets/quiz.js" defer></script>
  <script src="../assets/lang.js" defer></script>
</head>
<body>
<div class="page">
  <a class="home-link" href="../../../index.html">← Home</a>

  <header class="lesson-header">
    <div class="course-tag">
      <span class="lang-en">COURSE_CODE · CHAPTER · LESSON_LABEL</span>
      <span class="lang-th">COURSE_CODE · ชื่อบท · LESSON_LABEL</span>
    </div>
    <h1>
      <span class="lang-en">English Title</span>
      <span class="lang-th">ชื่อภาษาไทย</span>
    </h1>
    <p class="objective">
      <span class="lang-en"><strong>Goal:</strong> What the student will be able to do.</span>
      <span class="lang-th"><strong>จุดมุ่งหมาย:</strong> สิ่งที่นักเรียนจะทำได้หลังจบบทนี้</span>
    </p>
  </header>

  <!-- ═══ Section 1 ═══ -->
  <div class="lang-en">
    <h2>1. Section Title</h2>
    <p>Content here.</p>
    <div class="formula-box">
      <span class="label">Formula name</span>
      Formula content
    </div>
  </div>
  <div class="lang-th">
    <h2>1. หัวข้อภาษาไทย</h2>
    <p>เนื้อหาภาษาไทย</p>
    <div class="formula-box">
      <span class="label">ชื่อสูตร</span>
      เนื้อหาสูตร
    </div>
  </div>

  <!-- ═══ Quiz ═══ -->
  <div class="quiz-block" data-correct="A"
       data-feedback-correct-th="ถูกต้อง!"
       data-feedback-wrong-th="ไม่ถูก ลองใหม่">
    <p class="quiz-q">
      <span class="lang-en">Question text?</span>
      <span class="lang-th">คำถามภาษาไทย?</span>
    </p>
    <label><input type="radio" name="q1" value="A"> Option A</label>
    <label><input type="radio" name="q1" value="B"> Option B</label>
    <label><input type="radio" name="q1" value="C"> Option C</label>
    <button class="quiz-submit">Check</button>
    <div class="quiz-feedback"></div>
  </div>

  <!-- ═══ Formula Summary (end of lesson) ═══ -->
  <div class="formula-summary">
    <div class="fs-title">Formula Summary — Lesson XN</div>
    <div class="fs-row">
      <b>Name</b> formula here
    </div>
    <hr class="fs-sep">
    <div class="fs-row">
      <b>Name 2</b> another formula
    </div>
  </div>

  <!-- ═══ Navigation ═══ -->
  <nav class="nav-links">
    <a href="PREV_FILE.html">← Prev: XN Label</a>
    <a href="NEXT_FILE.html">Next: XN Label →</a>
  </nav>
  <!-- If no previous: use <span></span> instead of the first <a> -->
  <!-- If no next: use <span></span> instead of the second <a> -->

</div>
</body>
</html>
```

**Key CSS classes available in Math style.css:**

| Class | Purpose |
|-------|---------|
| `.formula-box` | Highlighted formula block with a `.label` span |
| `.key-concept` | Green-tinted callout box |
| `.worked-example` | Step-by-step solution block |
| `.quiz-block` | Quiz container (handled by quiz.js) |
| `.formula-summary` | Summary box at end of lesson |
| `.nav-links` | Prev/Next navigation row |
| `.lang-en` / `.lang-th` | Bilingual content (toggled by lang.js) |

---

## Template: Physics Lesson (data-i18n bilingual)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Lesson N — Title</title>
  <link rel="stylesheet" href="style.css" />
  <script>
    window.MathJax = {
      tex: { inlineMath: [['$','$']] },
      options: { skipHtmlTags: ['script','noscript','style','textarea'] }
    };
  </script>
  <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" async></script>
  <script src="quiz.js" defer></script>
  <script src="lang.js" defer></script>
</head>
<body>
<button class="lang-btn" id="lang-btn">ภาษาไทย</button>
<div class="page">
  <a class="home-link" href="../../index.html">← Home</a>

  <header class="lesson-header">
    <div class="course-tag">COURSE_CODE · MWIT &nbsp;|&nbsp; Lesson N of TOTAL</div>
    <h1 data-i18n="lN.h1">English Title</h1>
    <p class="objective" data-i18n-html="lN.obj">
      <strong>By the end of this lesson you will be able to:</strong> ...
    </p>
  </header>

  <h2 data-i18n="lN.h2.1">1. Section Title</h2>
  <p>Content here. Use $formula$ for inline math.</p>

  <nav class="nav-links">
    <a href="PREV_FILE.html">← P(N-1): Prev Title</a>
    <a href="NEXT_FILE.html">PN+1: Next Title →</a>
  </nav>

</div>
</body>
</html>
```

> Physics uses `data-i18n` keys — translations live in `lang.js`. Add new keys there when adding new lessons.

---

## Template: Civic / Thai-Only Lesson

```html
<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>บทที่ N — ชื่อบท</title>
  <link rel="stylesheet" href="style.css" />
  <script src="quiz.js" defer></script>
</head>
<body>
<div class="page">
  <a class="home-link" href="../../index.html">← Home</a>

  <header class="lesson-header">
    <div class="course-tag">SUBJECT · MWIT &nbsp;|&nbsp; บทที่ N จาก TOTAL</div>
    <h1>ชื่อบท</h1>
    <p class="objective"><strong>หลังจากบทนี้ คุณจะสามารถ:</strong> ...</p>
  </header>

  <h2>1. หัวข้อ</h2>
  <p>เนื้อหา</p>

  <nav class="nav-links">
    <a href="PREV_FILE.html">← C(N-1): ชื่อบทก่อน</a>
    <a href="NEXT_FILE.html">C(N+1): ชื่อบทถัดไป →</a>
  </nav>

</div>
</body>
</html>
```

---

## How to Add a Lesson to an Existing Subject

### Step 1 — Create the HTML file

Copy the correct template above into `lessons/NNNN-title.html`. Fill in content.

### Step 2 — Fix nav links in adjacent lessons

- Open the **previous** lesson → change its "Next" link to point to your new file.
- Open the **next** lesson → change its "Prev" link to point to your new file.

### Step 3 — Add it to the homepage (`index.html`)

Find the subject's `<div class="lesson-list">` and add a card:

```html
<a class="lesson-card" href="SubjectFolder/ChapterFolder/lessons/NNNN-title.html">
  <span class="lesson-num">X9</span>
  <div>
    <div class="lesson-title">English Title</div>
    <div class="lesson-sub">คำอธิบายภาษาไทย</div>
  </div>
  <span class="arrow">›</span>
</a>
```

Also update the lesson count in the subject header:
```html
<span class="subject-count">N lessons</span>
```

### Step 4 — Push

```bash
git add lessons/NNNN-title.html index.html
git commit -m "Add lesson XN: Title"
git push
```

---

## How to Add a Completely New Subject

### Step 1 — Create the folder structure

```
NewSubject/
└── lessons/
    ├── style.css      ← copy from Physics/lessons/style.css or Math/.../assets/style.css
    ├── quiz.js        ← copy from any existing lessons folder
    └── lang.js        ← copy if bilingual, skip if single-language
```

> Copy `style.css` and `quiz.js` from the most similar existing subject. Do **not** link to another subject's assets — each subject has its own copy.

### Step 2 — Create lesson files

Use the appropriate template. Set the `href` in `← Home` to `../../index.html` (2 levels deep) or `../../../index.html` (3 levels deep).

### Step 3 — Add a subject dropdown to `index.html`

Add a new `<div class="subject">` block before the closing `</div>` of `.page`. Choose an icon character for `.subject-icon`.

```html
<!-- ── NEW SUBJECT ── -->
<div class="subject">
  <div class="subject-header" onclick="toggle(this)">
    <div class="subject-icon">ICON</div>
    <div class="subject-meta">
      <div class="subject-name">Subject Name</div>
      <div class="subject-tag">Course Code · Course Name</div>
    </div>
    <div class="subject-right">
      <span class="subject-count">N lessons</span>
      <span class="chevron">›</span>
    </div>
  </div>
  <div class="lesson-list">

    <!-- Optional: chapter separator -->
    <div class="chapter-label">Chapter Name</div>

    <a class="lesson-card" href="NewSubject/lessons/0001-title.html">
      <span class="lesson-num">X1</span>
      <div>
        <div class="lesson-title">Lesson Title</div>
        <div class="lesson-sub">คำอธิบาย</div>
      </div>
      <span class="arrow">›</span>
    </a>

  </div>
</div>
```

**Icon ideas:** ∑ (math), ⚛ (physics), ⚖ (civic/law), 🧪 (chemistry), 📐 (geometry), ∫ (calculus), § (law)

### Step 4 — URL-encode folder names with Thai characters

Thai folder names in `href` must be URL-encoded. Example:

- Folder: `หน้าที่พลเมือง`
- Encoded: `%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%9E%E0%B8%A5%E0%B9%80%E0%B8%A1%E0%B8%B7%E0%B8%AD%E0%B8%87`

**Tip:** Use ASCII folder names (e.g. `Civic/`) to avoid encoding entirely.

### Step 5 — Push

```bash
git add NewSubject/ index.html
git commit -m "Add new subject: Subject Name (X lessons)"
git push
```

---

## Chapter Separators Inside a Dropdown

If one subject has multiple chapters, add `.chapter-label` divs between the lesson cards:

```html
<div class="lesson-list">
  <div class="chapter-label">Chapter 1 Name</div>
  <!-- lesson cards for chapter 1 -->
  <div class="chapter-label">Chapter 2 Name</div>
  <!-- lesson cards for chapter 2 -->
</div>
```

This is how Math works (Sequences & Series / The Derivative Function in one dropdown).

---

## Formula Summary Blocks

Add at the **end of every lesson**, before `<nav class="nav-links">`:

```html
<div class="formula-summary">
  <div class="fs-title">Formula Summary — XN</div>
  <div class="fs-row"><b>Name</b> formula</div>
  <hr class="fs-sep">
  <div class="fs-row"><b>Name 2</b> formula 2</div>
</div>
```

For the **last lesson in a chapter**, also add a chapter-level summary covering all lessons in that chapter, right after the lesson summary.

---

## Floating Buttons (Home & Translate)

Both buttons are `position: fixed` — they stay on screen while scrolling.

| Button | Position | Defined in |
|--------|----------|-----------|
| `← Home` (`.home-link`) | top-left | `style.css` in each subject |
| Translate (`.lang-toggle-btn`) | top-right | `lang.js` (injected by JS) |

The home button is an `<a>` tag placed right after `<div class="page">` in the HTML. The CSS in `style.css` positions it fixed. **Do not move it inside a different div** — it works because `position: fixed` removes it from normal flow.

---

## Quick Checklist for a New Lesson

- [ ] File saved to correct `lessons/` folder with `NNNN-title.html` name
- [ ] `← Home` href uses correct relative path (`../../` or `../../../`)
- [ ] Stylesheet path is correct (`style.css` or `../assets/style.css`)
- [ ] `quiz.js` and `lang.js` (if needed) linked with correct path
- [ ] `<nav class="nav-links">` has correct prev/next filenames
- [ ] Adjacent lessons updated with new prev/next links
- [ ] Formula summary added before nav
- [ ] Lesson card added to `index.html` with correct `href`, label, and title
- [ ] `subject-count` number updated in `index.html`
- [ ] `git add`, `git commit`, `git push` done
