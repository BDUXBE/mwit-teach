import re, pathlib, sys

# ── CSS BLOCKS ──────────────────────────────────────────────────────────────

CSS_MATH = """
/* Home link */
.home-link {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  font-family: var(--font-ui);
  font-size: 0.8rem;
  color: var(--muted);
  text-decoration: none;
  margin-bottom: 1.5rem;
  opacity: 0.8;
}
.home-link:hover { color: var(--accent); opacity: 1; }

/* Formula summary box */
.formula-summary {
  border: 1.5px solid var(--accent);
  border-radius: var(--radius);
  padding: 1.1rem 1.3rem;
  margin: 2.5rem 0 0.5rem;
  background: var(--surface);
}
.formula-summary .fs-title {
  font-family: var(--font-ui);
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.09em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 0.7rem;
}
.formula-summary .fs-row {
  display: flex;
  gap: 0.5rem;
  font-family: var(--font-mono);
  font-size: 0.88rem;
  line-height: 1.85;
  flex-wrap: wrap;
}
.formula-summary .fs-row b {
  color: var(--muted);
  font-family: var(--font-ui);
  font-weight: 600;
  min-width: 6rem;
  font-size: 0.8rem;
}
.formula-summary .fs-sep {
  border: none;
  border-top: 1px solid var(--border);
  margin: 0.6rem 0;
}
"""

CSS_PHYSICS = """
/* Home link */
.home-link {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  font-family: var(--font-ui);
  font-size: 0.8rem;
  color: var(--muted);
  text-decoration: none;
  margin-bottom: 1.5rem;
  opacity: 0.8;
}
.home-link:hover { color: var(--accent); opacity: 1; }

/* Formula summary box */
.formula-summary {
  border: 1.5px solid var(--accent);
  border-radius: var(--radius);
  padding: 1.1rem 1.3rem;
  margin: 2.5rem 0 0.5rem;
  background: var(--surface);
}
.formula-summary .fs-title {
  font-family: var(--font-ui);
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.09em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 0.7rem;
}
.formula-summary .fs-row {
  font-family: var(--font-mono);
  font-size: 0.88rem;
  line-height: 1.85;
}
.formula-summary .fs-sep {
  border: none;
  border-top: 1px solid var(--border);
  margin: 0.6rem 0;
}
"""

def append_css(path, block):
    p = pathlib.Path(path)
    content = p.read_text(encoding='utf-8')
    if '.home-link' in content:
        print(f"  [SKIP already has .home-link] {path}")
        return
    p.write_text(content.rstrip() + '\n' + block, encoding='utf-8')
    print(f"  [OK] CSS appended -> {path}")

append_css(r"D:\mwit\Teach\Math\Sequences and Series\assets\style.css", CSS_MATH)
append_css(r"D:\mwit\Teach\Math\The Derivative Function\assets\style.css", CSS_MATH)
append_css(r"D:\mwit\Teach\Physics\lessons\style.css", CSS_PHYSICS)

# ── FORMULA SUMMARIES ────────────────────────────────────────────────────────

FS = {}

FS["S1"] = """\
  <div class="formula-summary">
    <div class="fs-title">Lesson S1 — Formula Summary</div>
    <div class="lang-en">
      <div class="fs-row"><b>Arithmetic nᵗʰ term</b> aₙ = a₁ + (n−1)d</div>
      <div class="fs-row"><b>Arithmetic sum</b> Sₙ = n/2 · (a₁ + aₙ) = n/2 · (2a₁ + (n−1)d)</div>
      <hr class="fs-sep">
      <div class="fs-row"><b>Geometric nᵗʰ term</b> aₙ = a₁ · rⁿ⁻¹</div>
      <div class="fs-row"><b>Geometric sum</b> Sₙ = a₁(1 − rⁿ) / (1 − r) &nbsp;&nbsp; (r ≠ 1)</div>
      <hr class="fs-sep">
      <div class="fs-row"><b>Σ i</b> = n(n+1)/2</div>
      <div class="fs-row"><b>Σ i²</b> = n(n+1)(2n+1)/6</div>
      <div class="fs-row"><b>Σ i³</b> = [n(n+1)/2]²</div>
    </div>
    <div class="lang-th" hidden>
      <div class="fs-row"><b>พจน์ที่ n (เลขคณิต)</b> aₙ = a₁ + (n−1)d</div>
      <div class="fs-row"><b>ผลรวม (เลขคณิต)</b> Sₙ = n/2 · (a₁ + aₙ)</div>
      <hr class="fs-sep">
      <div class="fs-row"><b>พจน์ที่ n (เรขาคณิต)</b> aₙ = a₁ · rⁿ⁻¹</div>
      <div class="fs-row"><b>ผลรวม (เรขาคณิต)</b> Sₙ = a₁(1 − rⁿ) / (1 − r)</div>
      <hr class="fs-sep">
      <div class="fs-row"><b>Σ i</b> = n(n+1)/2</div>
      <div class="fs-row"><b>Σ i²</b> = n(n+1)(2n+1)/6</div>
      <div class="fs-row"><b>Σ i³</b> = [n(n+1)/2]²</div>
    </div>
  </div>
"""

FS["S2"] = """\
  <div class="formula-summary">
    <div class="fs-title">Lesson S2 — Formula Summary</div>
    <div class="lang-en">
      <div class="fs-row"><b>Converges</b> lim(n→∞) aₙ = L &nbsp;(L finite)</div>
      <div class="fs-row"><b>Diverges</b> lim(n→∞) aₙ = ±∞ or limit doesn’t exist</div>
      <hr class="fs-sep">
      <div class="fs-row"><b>Squeeze</b> aₙ ≤ bₙ ≤ cₙ and aₙ→L, cₙ→L &nbsp;⟹&nbsp; bₙ→L</div>
      <div class="fs-row"><b>Geometric</b> lim rⁿ = 0 if |r| &lt; 1 &nbsp;|&nbsp; diverges if |r| ≥ 1</div>
      <div class="fs-row"><b>lim n^p/eⁿ</b> = 0 &nbsp;for any p &nbsp;(exponential beats polynomial)</div>
    </div>
    <div class="lang-th" hidden>
      <div class="fs-row"><b>ลู่เข้า</b> lim(n→∞) aₙ = L &nbsp;(L มีค่าจำกัด)</div>
      <div class="fs-row"><b>ลู่ออก</b> ลิมิตไม่มีค่าหรือเป็น ±∞</div>
      <hr class="fs-sep">
      <div class="fs-row"><b>Squeeze</b> aₙ ≤ bₙ ≤ cₙ และ aₙ→L, cₙ→L &nbsp;⟹&nbsp; bₙ→L</div>
      <div class="fs-row"><b>เรขาคณิต</b> lim rⁿ = 0 ถ้า |r| &lt; 1 &nbsp;|&nbsp; ลู่ออกถ้า |r| ≥ 1</div>
    </div>
  </div>
"""

FS["S3"] = """\
  <div class="formula-summary">
    <div class="fs-title">Lesson S3 — Formula Summary</div>
    <div class="lang-en">
      <div class="fs-row"><b>Geometric series</b> Σ arⁿ = a/(1−r) &nbsp;if |r| &lt; 1 &nbsp;|&nbsp; diverges if |r| ≥ 1</div>
      <div class="fs-row"><b>Telescoping</b> write partial sums, cancel interior terms, take limit</div>
      <div class="fs-row"><b>Harmonic</b> Σ 1/n &nbsp;→&nbsp; DIVERGES (even though terms → 0)</div>
      <hr class="fs-sep">
      <div class="fs-row"><b>Key condition</b> if aₙ ↛ 0 then Σaₙ diverges (divergence test)</div>
    </div>
    <div class="lang-th" hidden>
      <div class="fs-row"><b>อนุกรมเรขาคณิต</b> Σ arⁿ = a/(1−r) ถ้า |r| &lt; 1 &nbsp;|&nbsp; ลู่ออกถ้า |r| ≥ 1</div>
      <div class="fs-row"><b>เทเลสโคป</b> เขียนผลรวมย่อย ตัดพจน์กลาง หาลิมิต</div>
      <div class="fs-row"><b>ฮาร์โมนิก</b> Σ 1/n &nbsp;→&nbsp; ลู่ออก (แม้พจน์ → 0)</div>
      <hr class="fs-sep">
      <div class="fs-row"><b>เงื่อนไขสำคัญ</b> ถ้า aₙ ↛ 0 แล้วอนุกรมลู่ออก</div>
    </div>
  </div>
"""

FS["S6"] = """\
  <div class="formula-summary">
    <div class="fs-title">Lesson S6 — Formula Summary · Convergence Tests</div>
    <div class="lang-en">
      <div class="fs-row"><b>Divergence test</b> if lim aₙ ≠ 0 → diverges &nbsp;(if = 0, inconclusive)</div>
      <div class="fs-row"><b>Ratio test</b> L = lim |aₙ₊₁/aₙ| &nbsp;→&nbsp; L&lt;1 conv · L&gt;1 div · L=1 ✗</div>
      <div class="fs-row"><b>Root test</b> L = lim |aₙ|^(1/n) &nbsp;→&nbsp; same conclusion as ratio</div>
      <div class="fs-row"><b>Alt. series</b> Σ(− 1)ⁿbₙ converges if bₙ → 0 monotonically</div>
      <div class="fs-row"><b>Comparison</b> 0 ≤ aₙ ≤ bₙ: bₙ conv → aₙ conv · aₙ div → bₙ div</div>
    </div>
    <div class="lang-th" hidden>
      <div class="fs-row"><b>Divergence test</b> ถ้า lim aₙ ≠ 0 → ลู่ออก &nbsp;(ถ้า = 0 สรุปไม่ได้)</div>
      <div class="fs-row"><b>Ratio test</b> L = lim |aₙ₊₁/aₙ| &nbsp;→&nbsp; L&lt;1 ลู่เข้า · L&gt;1 ลู่ออก · L=1 ✗</div>
      <div class="fs-row"><b>Root test</b> L = lim |aₙ|^(1/n) &nbsp;→&nbsp; สรุปเหมือน Ratio test</div>
      <div class="fs-row"><b>Alt. series</b> Σ(−1)ⁿbₙ ลู่เข้าถ้า bₙ → 0 แบบ monotone</div>
      <div class="fs-row"><b>Comparison</b> 0 ≤ aₙ ≤ bₙ: bₙ ลู่เข้า → aₙ ลู่เข้า · aₙ ลู่ออก → bₙ ลู่ออก</div>
    </div>
  </div>
  <div class="formula-summary" style="border-color: #b07d2e; background: #fdfaf5;">
    <div class="fs-title" style="color: #7a4e10;">Chapter Summary — Sequences &amp; Series (S1–S6)</div>
    <div class="lang-en">
      <div class="fs-row"><b>Arith. Sₙ</b> n(a₁+aₙ)/2 &nbsp;&nbsp;<b>Geo. Sₙ</b> a₁(1−rⁿ)/(1−r)</div>
      <div class="fs-row"><b>Geo. series</b> a/(1−r) if |r|&lt;1 &nbsp;&nbsp;<b>Harmonic</b> Σ1/n = ∞</div>
      <hr class="fs-sep">
      <div class="fs-row"><b>Div. test</b> aₙ↛0 → div &nbsp;&nbsp;<b>Ratio</b> L=lim|aₙ₊₁/aₙ| &nbsp;&nbsp;<b>Root</b> L=lim|aₙ|^(1/n)</div>
      <div class="fs-row"><b>L&lt;1</b> converges &nbsp;&nbsp;<b>L&gt;1</b> diverges &nbsp;&nbsp;<b>L=1</b> inconclusive</div>
    </div>
    <div class="lang-th" hidden>
      <div class="fs-row"><b>Sₙ เลขคณิต</b> n(a₁+aₙ)/2 &nbsp;&nbsp;<b>Sₙ เรขาคณิต</b> a₁(1−rⁿ)/(1−r)</div>
      <div class="fs-row"><b>อนุกรมเรขา</b> a/(1−r) ถ้า |r|&lt;1 &nbsp;&nbsp;<b>ฮาร์โมนิก</b> Σ1/n = ∞</div>
      <hr class="fs-sep">
      <div class="fs-row"><b>Div. test</b> aₙ↛0 → ลู่ออก &nbsp;&nbsp;<b>Ratio</b> L=lim|aₙ₊₁/aₙ| &nbsp;&nbsp;<b>Root</b> L=lim|aₙ|^(1/n)</div>
      <div class="fs-row"><b>L&lt;1</b> ลู่เข้า &nbsp;&nbsp;<b>L&gt;1</b> ลู่ออก &nbsp;&nbsp;<b>L=1</b> สรุปไม่ได้</div>
    </div>
  </div>
"""

FS["D1"] = """\
  <div class="formula-summary">
    <div class="fs-title">Lesson D1 — Formula Summary · Related Rates</div>
    <div class="lang-en">
      <div class="fs-row"><b>Circle area</b> A=πr² &nbsp;→&nbsp; dA/dt = 2πr · dr/dt</div>
      <div class="fs-row"><b>Sphere vol</b> V=⁴⁄₃πr³ &nbsp;→&nbsp; dV/dt = 4πr² · dr/dt</div>
      <div class="fs-row"><b>Cylinder</b> V=πr²h &nbsp;→&nbsp; dV/dt = πr²(dh/dt) + 2πrh(dr/dt)</div>
      <div class="fs-row"><b>Pythagoras</b> x²+y²=z² &nbsp;→&nbsp; 2x(dx/dt)+2y(dy/dt)=2z(dz/dt)</div>
      <hr class="fs-sep">
      <div class="fs-row"><b>Steps</b> ① diagram ② relate ③ diff w.r.t. t ④ sub values ⑤ solve</div>
    </div>
    <div class="lang-th" hidden>
      <div class="fs-row"><b>พื้นที่วงกลม</b> A=πr² &nbsp;→&nbsp; dA/dt = 2πr · dr/dt</div>
      <div class="fs-row"><b>ปริมาตรทรงกลม</b> V=⁴⁄₃πr³ &nbsp;→&nbsp; dV/dt = 4πr² · dr/dt</div>
      <div class="fs-row"><b>ทรงกระบอก</b> V=πr²h &nbsp;→&nbsp; dV/dt = πr²(dh/dt) + 2πrh(dr/dt)</div>
      <div class="fs-row"><b>พีทาโกรัส</b> x²+y²=z² &nbsp;→&nbsp; 2x(dx/dt)+2y(dy/dt)=2z(dz/dt)</div>
      <hr class="fs-sep">
      <div class="fs-row"><b>ขั้นตอน</b> ① วาดภาพ ② เชื่อมโยง ③ diff เทียบ t ④ แทนค่า ⑤ แก้สมการ</div>
    </div>
  </div>
"""

FS["D2"] = """\
  <div class="formula-summary">
    <div class="fs-title">Lesson D2 — Formula Summary · L’Hôpital’s Rule</div>
    <div class="lang-en">
      <div class="fs-row"><b>Rule</b> if 0/0 or ∞/∞ &nbsp;→&nbsp; lim f/g = lim f′/g′</div>
      <div class="fs-row"><b>Check first</b> sub x=a → must get 0/0 or ±∞/±∞</div>
      <div class="fs-row"><b>Apply again</b> if still indeterminate after first application</div>
      <hr class="fs-sep">
      <div class="fs-row"><b>Other forms</b> 0·∞ · ∞−∞ · 0⁰ · 1^∞ · ∞⁰ → rewrite as 0/0 or ∞/∞ first</div>
    </div>
    <div class="lang-th" hidden>
      <div class="fs-row"><b>กฎ</b> ถ้า 0/0 หรือ ∞/∞ &nbsp;→&nbsp; lim f/g = lim f′/g′</div>
      <div class="fs-row"><b>ตรวจก่อน</b> แทน x=a → ต้องได้ 0/0 หรือ ±∞/±∞</div>
      <div class="fs-row"><b>ใช้ซ้ำ</b> ถ้ายังเป็นรูปอนิยามหลังใช้ครั้งแรก ให้ใช้อีกครั้ง</div>
      <hr class="fs-sep">
      <div class="fs-row"><b>รูปอื่นๆ</b> 0·∞ · ∞−∞ · 0⁰ · 1^∞ · ∞⁰ → แปลงให้เป็น 0/0 หรือ ∞/∞ ก่อน</div>
    </div>
  </div>
"""

FS["D4"] = """\
  <div class="formula-summary">
    <div class="fs-title">Lesson D4 — Formula Summary · Function Analysis I</div>
    <div class="lang-en">
      <div class="fs-row"><b>f′&gt;0</b> increasing &nbsp;&nbsp;<b>f′&lt;0</b> decreasing &nbsp;&nbsp;<b>f′=0</b> critical point</div>
      <div class="fs-row"><b>+→−</b> local max &nbsp;&nbsp;<b>−→+</b> local min &nbsp;&nbsp;no change → neither</div>
      <hr class="fs-sep">
      <div class="fs-row"><b>f″&gt;0</b> concave up (∪) &nbsp;&nbsp;<b>f″&lt;0</b> concave down (∩)</div>
      <div class="fs-row"><b>2nd deriv test</b> f′(c)=0 &amp; f″(c)&gt;0 → min &nbsp;|&nbsp; f″(c)&lt;0 → max</div>
      <div class="fs-row"><b>Inflection pt</b> f″ changes sign at x=c</div>
    </div>
    <div class="lang-th" hidden>
      <div class="fs-row"><b>f′&gt;0</b> เพิ่ม &nbsp;&nbsp;<b>f′&lt;0</b> ลด &nbsp;&nbsp;<b>f′=0</b> จุดวิกฤต</div>
      <div class="fs-row"><b>+→−</b> สูงสุดเฉพาะที่ &nbsp;&nbsp;<b>−→+</b> ต่ำสุดเฉพาะที่ &nbsp;&nbsp;ไม่เปลี่ยน → ไม่ใช่สุดขีด</div>
      <hr class="fs-sep">
      <div class="fs-row"><b>f″&gt;0</b> เว้าขึ้น (∪) &nbsp;&nbsp;<b>f″&lt;0</b> เว้าลง (∩)</div>
      <div class="fs-row"><b>2nd deriv test</b> f′(c)=0 &amp; f″(c)&gt;0 → ต่ำสุด &nbsp;|&nbsp; f″(c)&lt;0 → สูงสุด</div>
      <div class="fs-row"><b>จุดเปลี่ยนความเว้า</b> f″ เปลี่ยนเครื่องหมายที่ x=c</div>
    </div>
  </div>
  <div class="formula-summary" style="border-color: #b07d2e; background: #fdfaf5;">
    <div class="fs-title" style="color: #7a4e10;">Chapter Summary — The Derivative Function (D1–D4)</div>
    <div class="lang-en">
      <div class="fs-row"><b>Related rates</b> differentiate both sides w.r.t. t, then substitute</div>
      <div class="fs-row"><b>L’Hôpital</b> 0/0 or ∞/∞ → lim f/g = lim f′/g′ &nbsp;(check form first!)</div>
      <hr class="fs-sep">
      <div class="fs-row"><b>Monotonicity</b> f′&gt;0 ↑ · f′&lt;0 ↓ · sign change at c → extremum</div>
      <div class="fs-row"><b>Concavity</b> f″&gt;0 ∪ · f″&lt;0 ∩ · sign change → inflection point</div>
    </div>
    <div class="lang-th" hidden>
      <div class="fs-row"><b>Related rates</b> หาอนุพันธ์ทั้งสองข้างเทียบ t แล้วแทนค่า</div>
      <div class="fs-row"><b>โลปีตาล</b> 0/0 หรือ ∞/∞ → lim f/g = lim f′/g′ &nbsp;(ตรวจรูปแบบก่อน!)</div>
      <hr class="fs-sep">
      <div class="fs-row"><b>เพิ่ม/ลด</b> f′&gt;0 ↑ · f′&lt;0 ↓ · เปลี่ยนเครื่องหมายที่ c → ค่าสุดขีด</div>
      <div class="fs-row"><b>ความเว้า</b> f″&gt;0 ∪ · f″&lt;0 ∩ · เปลี่ยนเครื่องหมาย → จุดเปลี่ยนความเว้า</div>
    </div>
  </div>
"""

FS["P1"] = """\
  <div class="formula-summary">
    <div class="fs-title">Lesson P1 — Key Concepts · Origin of Special Relativity</div>
    <div class="fs-row"><b>Postulate 1</b> Laws of physics are the same in all inertial frames</div>
    <div class="fs-row"><b>Postulate 2</b> Speed of light c = 3×10⁸ m/s is constant for all observers</div>
    <div class="fs-row"><b>M-M result</b> No ether detected — c independent of Earth’s motion</div>
    <div class="fs-row"><b>Consequence</b> Space and time are not absolute — they depend on the observer</div>
  </div>
"""

FS["P2"] = """\
  <div class="formula-summary">
    <div class="fs-title">Lesson P2 — Formula Summary · Time Dilation &amp; Length Contraction</div>
    <div class="fs-row"><b>Lorentz factor</b> γ = 1 / √(1 − v²/c²) &nbsp;&nbsp; γ ≥ 1 always</div>
    <div class="fs-row"><b>Time dilation</b> Δt = γ · Δt₀ &nbsp;&nbsp;(moving clock runs slow)</div>
    <div class="fs-row"><b>Length contraction</b> L = L₀ / γ &nbsp;&nbsp;(moving rod is shorter)</div>
    <hr class="fs-sep">
    <div class="fs-row"><b>Proper time</b> Δt₀ measured in the rest frame of the event</div>
    <div class="fs-row"><b>Proper length</b> L₀ measured in the rest frame of the object</div>
  </div>
"""

FS["P3"] = """\
  <div class="formula-summary">
    <div class="fs-title">Lesson P3 — Formula Summary · Lorentz Transformation</div>
    <div class="fs-row"><b>Position</b> x′ = γ(x − vt)</div>
    <div class="fs-row"><b>Time</b> t′ = γ(t − vx/c²)</div>
    <div class="fs-row"><b>Inverse</b> x = γ(x′ + vt′) &nbsp;&nbsp; t = γ(t′ + vx′/c²)</div>
    <hr class="fs-sep">
    <div class="fs-row"><b>Velocity addition</b> u′ = (u − v) / (1 − uv/c²)</div>
    <div class="fs-row"><b>Simultaneity</b> events simultaneous in S may not be in S′</div>
  </div>
"""

FS["P4"] = """\
  <div class="formula-summary">
    <div class="fs-title">Lesson P4 — Formula Summary · Relativistic Momentum &amp; Energy</div>
    <div class="fs-row"><b>Momentum</b> p = γmv</div>
    <div class="fs-row"><b>Total energy</b> E = γmc²</div>
    <div class="fs-row"><b>Rest energy</b> E₀ = mc²</div>
    <div class="fs-row"><b>Kinetic energy</b> KE = (γ − 1)mc²</div>
    <hr class="fs-sep">
    <div class="fs-row"><b>Energy-momentum</b> E² = (pc)² + (mc²)²</div>
    <div class="fs-row"><b>Massless (photon)</b> E = pc</div>
  </div>
"""

FS["P5"] = """\
  <div class="formula-summary">
    <div class="fs-title">Lesson P5 — Formula Summary · Blackbody Radiation &amp; Quantum</div>
    <div class="fs-row"><b>Stefan-Boltzmann</b> P = σAT⁴ &nbsp;&nbsp;(σ = 5.67×10⁻⁸ W/m²K⁴)</div>
    <div class="fs-row"><b>Wien’s law</b> λ_max · T = 2.898×10⁻³ m·K</div>
    <div class="fs-row"><b>Planck energy</b> E = hf = hc/λ &nbsp;&nbsp;(h = 6.626×10⁻³⁴ J·s)</div>
    <hr class="fs-sep">
    <div class="fs-row"><b>Photoelectric</b> hf = φ + KE_max</div>
    <div class="fs-row"><b>Threshold freq</b> f₀ = φ/h &nbsp;&nbsp;(minimum to eject electron)</div>
  </div>
"""

FS["P6"] = """\
  <div class="formula-summary">
    <div class="fs-title">Lesson P6 — Exam Review Summary</div>
    <div class="fs-row"><b>γ</b> = 1/√(1−v²/c²) &nbsp;&nbsp;<b>Δt</b> = γΔt₀ &nbsp;&nbsp;<b>L</b> = L₀/γ</div>
    <div class="fs-row"><b>Lorentz</b> x′=γ(x−vt) · t′=γ(t−vx/c²) · u′=(u−v)/(1−uv/c²)</div>
    <div class="fs-row"><b>Energy</b> E=γmc² · p=γmv · E²=(pc)²+(mc²)²</div>
    <div class="fs-row"><b>Blackbody</b> P=σAT⁴ · λ_max·T=2.898×10⁻³ · E=hf</div>
  </div>
  <div class="formula-summary" style="border-color: #2e5cb0; background: #f5f8ff;">
    <div class="fs-title" style="color: #1a3a7a;">Chapter Summary — Modern Physics (P1–P6)</div>
    <div class="fs-row"><b>Postulates</b> same physics in all inertial frames · c constant</div>
    <hr class="fs-sep">
    <div class="fs-row"><b>γ</b> = 1/√(1−β²) &nbsp;where β=v/c &nbsp;&nbsp;<b>Δt</b>=γΔt₀ &nbsp;&nbsp;<b>L</b>=L₀/γ</div>
    <div class="fs-row"><b>x′</b>=γ(x−vt) &nbsp;<b>t′</b>=γ(t−vx/c²) &nbsp;<b>u′</b>=(u−v)/(1−uv/c²)</div>
    <hr class="fs-sep">
    <div class="fs-row"><b>E</b>=γmc² &nbsp;<b>p</b>=γmv &nbsp;<b>E₀</b>=mc² &nbsp;<b>E²</b>=(pc)²+(mc²)²</div>
    <div class="fs-row"><b>P</b>=σAT⁴ &nbsp;<b>λT</b>=2.898×10⁻³ &nbsp;<b>E</b>=hf &nbsp;<b>hf</b>=φ+KE_max</div>
  </div>
"""

# ── FILE MAP ─────────────────────────────────────────────────────────────────

BASE = r"D:\mwit\Teach"

FILES = [
    # (rel_path, home_href, formula_key_or_None)
    (r"Math\Sequences and Series\lessons\0000-finite-sequences-and-partial-sums.html",
     "../../../index.html", "S1"),
    (r"Math\Sequences and Series\lessons\0001-infinite-sequences.html",
     "../../../index.html", "S2"),
    (r"Math\Sequences and Series\lessons\0002-infinite-series.html",
     "../../../index.html", "S3"),
    (r"Math\Sequences and Series\lessons\0004-convergence-tests.html",
     "../../../index.html", "S6"),
    (r"Math\The Derivative Function\lessons\0001-lhopitals-rule.html",
     "../../../index.html", "D2"),
    (r"Math\The Derivative Function\lessons\0002-function-analysis.html",
     "../../../index.html", "D4"),
    (r"Math\The Derivative Function\lessons\0003-related-rates.html",
     "../../../index.html", "D1"),
    (r"Physics\lessons\0001-origin-of-special-relativity.html",
     "../../index.html", "P1"),
    (r"Physics\lessons\0002-time-dilation-length-contraction.html",
     "../../index.html", "P2"),
    (r"Physics\lessons\0003-lorentz-transformation.html",
     "../../index.html", "P3"),
    (r"Physics\lessons\0004-relativistic-momentum-energy.html",
     "../../index.html", "P4"),
    (r"Physics\lessons\0005-blackbody-radiation.html",
     "../../index.html", "P5"),
    (r"Physics\lessons\0006-exam-review.html",
     "../../index.html", "P6"),
    (r"หน้าที่พลเมือง\lessons\0001-kwamru-phunthan-kotmai.html",
     "../../index.html", None),
    (r"หน้าที่พลเมือง\lessons\0002-rat-ratthathammanun-kotmai-pokkhrong.html",
     "../../index.html", None),
    (r"หน้าที่พลเมือง\lessons\0003-kotmai-aya.html",
     "../../index.html", None),
    (r"หน้าที่พลเมือง\lessons\0004-kotmai-phaeng-bukhkhon.html",
     "../../index.html", None),
]

# ── PROCESS EACH FILE ────────────────────────────────────────────────────────

for (rel, href, fs_key) in FILES:
    path = pathlib.Path(BASE) / rel
    try:
        content = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"  [MISS] {rel}")
        continue

    changed = False

    # 1) Insert home link after <div class="page">
    HOME_LINK = f'  <a class="home-link" href="{href}">← Home</a>\n'
    if 'class="home-link"' not in content:
        new_content, n = re.subn(
            r'(<div class="page">)\n',
            r'\1\n' + HOME_LINK,
            content, count=1
        )
        if n == 0:
            new_content, n = re.subn(
                r'(<div class="page">)',
                r'\1\n' + HOME_LINK,
                content, count=1
            )
        if n:
            content = new_content
            changed = True
            print(f"  [HOME OK] {rel}")
        else:
            print(f"  [HOME FAIL - no <div class=\"page\">] {rel}")
    else:
        print(f"  [HOME SKIP - already present] {rel}")

    # 2) Insert formula summary before <nav class="nav-links">
    if fs_key and fs_key in FS:
        if 'class="formula-summary"' not in content:
            fs_block = FS[fs_key]
            new_content, n = re.subn(
                r'(  <nav class="nav-links">)',
                fs_block + r'\1',
                content, count=1
            )
            if n:
                content = new_content
                changed = True
                print(f"  [FS   OK] {rel}")
            else:
                print(f"  [FS FAIL - no nav-links] {rel}")
        else:
            print(f"  [FS SKIP - already present] {rel}")

    if changed:
        path.write_text(content, encoding='utf-8')

print("\nAll done.")
