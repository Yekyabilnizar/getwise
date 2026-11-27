"""English versions of the wave-3 guides. Keys are the Indonesian slugs."""
from articles_more import T

TIP = lambda t: f'<div class="note info"><b>Tip:</b> {t}</div>'
NEW_EN = {}


def A(sid, **kw):
    NEW_EN[sid] = kw


A("cara-menghitung-pesangon", slug="how-to-calculate-severance-pay-indonesia",
  title="How to Calculate Severance Pay in Indonesia (PP 35/2021): Formula, Tables, and Tax",
  h1="How to Calculate Severance Pay in Indonesia",
  desc="Guide to calculating severance (uang pesangon), long-service pay (UPMK), and compensation of rights (UPH) under PP 35/2021, with tables, an example, multipliers by termination reason, and severance tax.",
  lead="Termination of employment can happen to anyone. Know your rights so you aren't short-changed when severance is paid.",
  body=[
      ("Three components of termination pay", """<p>Under the Manpower Law as amended by the Job Creation Law, and its implementing regulation <b>PP 35/2021</b>, a terminated employee may be entitled to three components:</p>
<ul><li><b>Severance pay (uang pesangon, UP)</b>, based on length of service.</li>
<li><b>Long-service pay (uang penghargaan masa kerja, UPMK)</b>, for at least 3 years of service.</li>
<li><b>Compensation of rights (uang penggantian hak, UPH)</b>, such as unused annual leave and travel costs back to the place of hire for the employee and family.</li></ul>
<p>The basis is <b>monthly wages</b>: base salary plus fixed allowances, excluding overtime and variable allowances.</p>"""),
      ("Severance and long-service pay tables", T(["Length of service", "Severance pay"], [
          ["Less than 1 year", "1 month's wages"], ["1 to under 2 years", "2 months"], ["2 to under 3 years", "3 months"],
          ["3 to under 4 years", "4 months"], ["4 to under 5 years", "5 months"], ["5 to under 6 years", "6 months"],
          ["6 to under 7 years", "7 months"], ["7 to under 8 years", "8 months"], ["8 years or more", "9 months"]])
       + T(["Length of service", "Long-service pay (UPMK)"], [
          ["3 to under 6 years", "2 months' wages"], ["6 to under 9 years", "3 months"], ["9 to under 12 years", "4 months"],
          ["12 to under 15 years", "5 months"], ["15 to under 18 years", "6 months"], ["18 to under 21 years", "7 months"],
          ["21 to under 24 years", "8 months"], ["24 years or more", "10 months"]])),
      ("Multipliers by reason for termination", """<p>The final amount is not always the table figure. PP 35/2021 sets different <b>multipliers</b> depending on the reason for termination. Some examples:</p>
<ul><li><b>Efficiency to prevent losses</b>: 1× severance, plus UPMK and UPH.</li>
<li><b>Efficiency because the company is making losses</b>: 0.5× severance, plus UPMK and UPH.</li>
<li><b>Retirement age</b>: 1.75× severance, plus UPMK and UPH.</li>
<li><b>Death of the employee</b>: 2× severance to the heirs, plus UPMK and UPH.</li>
<li><b>Voluntary resignation</b>: no severance or UPMK, but entitled to UPH and separation pay set in the employment agreement or company regulations.</li></ul>
<p>Other reasons, such as closure, bankruptcy, mergers, or serious misconduct, each have their own rules. A collective labor agreement may also set more favorable amounts. If in doubt, consult the local manpower office or a union.</p>"""),
      ("Worked example", """<p>A permanent employee with wages of <b>Rp8,000,000</b> and <b>7 years 4 months</b> of service is terminated for efficiency to prevent losses, with 6 days of annual leave remaining.</p>""" + T(["Component", "Calculation", "Amount"], [
          ["Severance (7–8 years of service)", "1 × 8 × Rp8,000,000", "Rp64,000,000"], ["UPMK (6–9 years of service)", "3 × Rp8,000,000", "Rp24,000,000"],
          ["UPH for leave (6 days)", "6/25 × Rp8,000,000 (assuming a 25-working-day divisor)", "Rp1,920,000"], ["=Total before tax", "", "Rp89,920,000"]]) + """
<p>The divisor for the daily wage can differ by work pattern and company policy, so the UPH figure may vary slightly.</p>"""),
      ("Tax on severance", """<p>Severance, UPMK, and UPH paid as a lump sum are subject to <b>final PPh 21</b> at tiered rates on the gross amount:</p>""" + T(["Income bracket", "Rate"], [
          ["Up to Rp50 million", "0%"], ["Above Rp50 million to Rp100 million", "5%"], ["Above Rp100 million to Rp500 million", "15%"], ["Above Rp500 million", "25%"]]) + """
<p>In the example above, the Rp89,920,000 total is taxed: the first Rp50 million at 0%, and the next Rp39,920,000 at 5%, or Rp1,996,000. Net severance received is about <b>Rp87,924,000</b>. Because the tax is final, severance is not added to salary when calculating annual tax.</p>"""),
      ("Tips if you are laid off", "<ul>"
       "<li><b>Ask for a written calculation</b> from the company and check it against the tables and the termination reason.</li>"
       "<li><b>Make sure the wage base is right</b>: base salary plus fixed allowances.</li>"
       "<li><b>Don't sign in a hurry</b> if anything is unclear. You have the right to bipartite negotiation.</li>"
       "<li><b>Claim JKP and JHT</b> at BPJS Employment. JKP is only for laid-off employees and has a filing deadline.</li>"
       "<li><b>Manage severance wisely</b>: set aside several months of emergency funds, pay off high-interest debt, then consider investing or a business.</li>"
       "<li><b>Ask for a reference letter (paklaring)</b> and your tax withholding slip for your next job and tax return.</li></ul>"
       + TIP("also calculate your take-home pay at your next job with the take-home pay calculator, so your post-layoff plan is realistic.")),
      ("Conclusion", """<p>Termination pay consists of severance, long-service pay, and compensation of rights, with amounts set by length of service and the reason for termination. Calculate it on the correct wage, check the multiplier, and account for the final tax so you know the net amount you'll receive. With good preparation, severance can bridge you to your next job or business.</p>"""),
  ],
  faq=[("Do contract employees get severance?", "Fixed-term (PKWT) employees don't get severance, but are entitled to compensation when the contract ends if they worked at least 1 month, equal to months of service divided by 12 times monthly wages."),
       ("Can severance be paid in installments?", "Ideally it is paid in full. If otherwise agreed, make sure it is in writing and doesn't disadvantage the employee."),
       ("Does severance affect my JHT claim?", "No. Severance is paid by the company, while JHT is your balance at BPJS Employment. They are separate rights.")])

A("cara-menghitung-zakat-penghasilan", slug="how-to-calculate-income-zakat",
  title="How to Calculate Income Zakat (Zakat Profesi): Nisab, Rate, and Examples",
  h1="How to Calculate Income Zakat",
  desc="Guide to income or professional zakat in Indonesia: definition, nisab equal to 85 grams of gold, the 2.5% rate, monthly and annual calculation, and zakat as a tax deduction.",
  lead="For Muslims, income zakat is an obligation on salary and other earnings that reach the nisab. Here is how to calculate it.",
  body=[
      ("What is income zakat?", """<p><b>Income zakat</b>, often called professional zakat (zakat profesi), is paid on income such as salary, fees, wages, and other service income. In Indonesia, calculation guidance follows MUI fatwas and the rules of BAZNAS, the official zakat agency.</p>
<p>It is obligatory once income reaches the <b>nisab</b> (a minimum threshold), at a <b>rate of 2.5%</b>. Many people pay it monthly on payday so it is lighter and regular.</p>"""),
      ("Nisab and rate", """<p>The nisab for income zakat equals the value of <b>85 grams of gold per year</b>. Because gold prices change, the rupiah value of the nisab changes too. BAZNAS usually announces the reference value.</p>
<div class="formula">Annual nisab  = 85 grams × gold price per gram
Monthly nisab = annual nisab ÷ 12
Zakat         = 2.5% × income (if ≥ nisab)</div>
<p>Example assuming a gold price of Rp2,000,000 per gram (illustration only): annual nisab Rp170,000,000, or about <b>Rp14,166,667 per month</b>.</p>"""),
      ("Worked examples", T(["Situation", "Monthly income", "Reaches nisab?", "Monthly zakat"], [
          ["Employee A", "Rp10,000,000", "No (below Rp14.17 million)", "Not obligatory; charity encouraged"],
          ["Employee B", "Rp15,000,000", "Yes", "2.5% × Rp15,000,000 = Rp375,000"],
          ["Employee C", "Rp25,000,000", "Yes", "2.5% × Rp25,000,000 = Rp625,000"]]) + """
<p>Views differ on whether zakat is calculated on gross income or after basic needs. BAZNAS guidance generally uses gross income. If unsure, follow the guidance of the zakat institution you pay through or consult a scholar.</p>"""),
      ("Zakat as a tax deduction", """<p>Zakat paid through an <b>official zakat agency or institution</b> recognized by the government can be deducted from gross income in tax calculations, under the tax rules. A valid payment receipt is required, such as a Zakat Payment Receipt (BSZ) with the payer's identity.</p>
<p>If your employer deducts zakat from salary and pays it to an official institution, the deduction can be reflected in PPh 21. If you pay it yourself, keep the receipt for your annual tax return. Zakat given directly to recipients without an official institution cannot be deducted for tax, although it remains valid religiously.</p>"""),
      ("Tips for paying income zakat", "<ul>"
       "<li><b>Calculate on payday</b> and set it aside before spending on anything else.</li>"
       "<li><b>Use official institutions</b> so distribution is well targeted and the receipt can be used for tax.</li>"
       "<li><b>Put zakat in your budget</b> as its own line at the start, before splitting the rest of your income.</li>"
       "<li><b>Remember irregular income</b> such as bonuses, THR, and fees; zakat applies to them too if the nisab is reached.</li>"
       "<li><b>Keep payment receipts</b> for your annual tax return.</li></ul>"
       + TIP("check your take-home pay with the take-home pay calculator to build a budget that includes zakat.")),
      ("Conclusion", """<p>Income zakat is 2.5% of income that reaches the nisab of 85 grams of gold per year. Paying it monthly through an official institution makes it lighter and more orderly, and it can reduce taxable income. Make zakat the first line in your budget so it is never missed.</p>"""),
  ],
  faq=[("Is income zakat the same as zakat fitrah?", "No. Zakat fitrah is paid once a year before Eid al-Fitr per person, while income zakat is calculated from earnings."),
       ("What if my income varies?", "You can add up a year's income, compare it with the annual nisab, and pay 2.5% of the total."),
       ("Can zakat be paid through an app?", "Yes, as long as it goes through the official channel of a licensed zakat institution so the receipt is valid.")])

A("panduan-kta-kredit-tanpa-agunan", slug="unsecured-personal-loans-kta-guide",
  title="Unsecured Personal Loans (KTA) in Indonesia: How They Work, Interest, Requirements, and Tips",
  h1="A Guide to KTA: Unsecured Bank Loans",
  desc="What KTA is, how to calculate flat and effective interest, application requirements, provision and insurance fees, comparison with other loans, and tips for using KTA safely.",
  lead="A KTA can provide quick funds without collateral, but the interest isn't small. Understand how it works before applying.",
  body=[
      ("What is a KTA?", """<p>A <b>KTA (Kredit Tanpa Agunan)</b> is a bank loan that doesn't require collateral such as a house or vehicle. Approval is based on income, credit history, and repayment capacity. The limit is usually several times monthly salary, with a 1 to 5 year term and fixed monthly installments.</p>
<p>Because there is no collateral, the bank's risk is higher, so KTA rates are higher than mortgages or secured loans, but generally lower than unpaid credit card balances or short-term online loans.</p>"""),
      ("Flat monthly rates and effective rates", """<p>KTA rates are often quoted as a <b>flat rate per month</b>, such as 1% per month. That looks small, but equals a much higher effective rate.</p>""" + T(["Item", "Amount"], [
          ["Loan", "Rp50,000,000"], ["Term", "36 months"], ["Flat interest 1% per month (12% per year)", "Rp500,000 × 36 = Rp18,000,000"],
          ["Monthly installment", "Rp1,888,889"], ["=Equivalent effective rate", "about 21.2% per year"]]) + """
<p>Always convert an offer to the effective rate before comparing it with other loans. The calculation works the same way as a flat-rate vehicle loan.</p>"""),
      ("Requirements and fees", """<ul><li><b>General requirements</b>: Indonesian citizen, at least 21, minimum income set by the bank, a certain length of employment, ID card, tax ID, payslips or bank statements.</li>
<li><b>Good credit history</b> in SLIK OJK.</li>
<li><b>Provision fee</b>, usually a percentage of the limit deducted at disbursement.</li>
<li><b>Admin fee</b> and sometimes <b>credit life insurance</b>.</li>
<li><b>Late fees</b> and <b>early-repayment penalties</b>.</li></ul>
<p>Note that the money you receive may be less than the approved limit because provision and admin fees are deducted upfront.</p>"""),
      ("When does a KTA make sense?", """<ul><li><b>Paying off more expensive debt</b>, such as accumulated credit card balances or online loans, lowering total interest (debt consolidation).</li>
<li><b>Important, planned needs</b> such as education costs or urgent renovations, when no cheaper source is available.</li>
<li><b>Business capital</b> with clear cash flow projections that can cover installments.</li></ul>
<p>A KTA is a poor fit for lifestyle spending, holidays, or consumer goods that lose value quickly.</p>"""),
      ("Tips for using a KTA safely", "<ul>"
       "<li><b>Borrow only what you need</b>, not the full limit offered.</li>"
       "<li><b>Keep total installments</b> on all debts below 30% of income.</li>"
       "<li><b>Compare several banks</b> by effective rate, provision, and penalties.</li>"
       "<li><b>Choose a short term</b> if installments remain comfortable, to reduce total interest.</li>"
       "<li><b>Beware of phone or message offers</b> asking for personal data or upfront fees. Apply directly through the bank's official channels.</li></ul>"
       + TIP("calculate the effective rate of a flat-rate offer with the vehicle loan calculator; enter a 0% down payment and the annual flat rate.")),
      ("Conclusion", """<p>A KTA gives access to funds without collateral and with fixed installments, but its rate is relatively high and often quoted as a flat monthly rate. Calculate the effective rate, include all fees, and use a KTA for important needs or to replace more expensive debt, not for consumption.</p>"""),
  ],
  faq=[("How long does a KTA take?", "From a few days to two weeks, depending on documents and the bank. Some banks offer faster digital processes."),
       ("Can a KTA be repaid early?", "Yes, usually with a penalty. Ask how remaining interest is calculated on early repayment."),
       ("Can self-employed people apply?", "Yes, with business documents and bank statements as proof of income. Requirements are usually stricter.")])

A("asuransi-kesehatan-swasta-vs-bpjs", slug="private-health-insurance-vs-bpjs",
  title="Private Health Insurance vs. BPJS Health in Indonesia: Differences and How to Choose",
  h1="Private Health Insurance or BPJS Health?",
  desc="Compare BPJS Health and private health insurance in Indonesia: coverage, premiums, referral system, plan types, key terms like waiting periods and limits, and how to choose.",
  lead="BPJS Health is mandatory, while private insurance is optional. When do you need both, and how do you choose?",
  body=[
      ("The role of BPJS Health", """<p>BPJS Health is Indonesia's mandatory national health insurance. Its strengths: affordable contributions, broad coverage including chronic and high-cost conditions, and no exclusion for pre-existing conditions. Services follow a <b>tiered referral system</b>, starting at primary care.</p>
<p>Its limitations usually involve queues, choice of hospitals and doctors, and room comfort. That's where private insurance is often considered as a complement.</p>"""),
      ("Quick comparison", T(["Aspect", "BPJS Health", "Private insurance"], [
          ["Nature", "Mandatory", "Voluntary"], ["Cost", "Fixed contribution or % of wages", "Premium depends on age, plan, and health"],
          ["Access", "Tiered referrals", "Usually direct to partner hospitals"], ["Pre-existing conditions", "Covered", "Often excluded or subject to waiting periods"],
          ["Benefit limits", "Per service package", "Annual or per-item limits"], ["Comfort", "By class or standard room", "Choice of room and hospital"]])),
      ("Key terms in a health insurance policy", """<ul><li><b>Waiting period</b>: an initial period when certain illnesses aren't covered, for example 30 days for general illness and 12 months for specific conditions.</li>
<li><b>Pre-existing condition</b>: an illness present before the policy started; often excluded.</li>
<li><b>Annual limit</b> and <b>inner limit</b>: the yearly total cap and caps per cost type (room, surgery, medicine).</li>
<li><b>As charged</b>: costs covered as billed up to the annual limit, without per-item caps.</li>
<li><b>Cashless</b> and <b>reimbursement</b>: paid directly by the insurer at partner hospitals, or you pay first and claim back.</li>
<li><b>Coordination of benefits (COB)</b>: cooperation with BPJS Health, where BPJS covers part of the cost and the private insurer covers the difference.</li></ul>"""),
      ("How to choose", """<ol><li><b>Make sure BPJS Health is active first</b> as your base protection.</li>
<li><b>Check employer insurance</b>. Many companies already provide health cover; learn what it covers before buying your own.</li>
<li><b>Define your needs</b>: inpatient only, or also outpatient, dental, and maternity.</li>
<li><b>Compare benefits, not just premiums</b>: limits, hospital network, exclusions, and waiting periods.</li>
<li><b>Avoid mixing protection and investment</b> if protection is your main goal; pure insurance usually gives more cover for the same premium.</li>
<li><b>Choose an OJK-supervised insurer</b> with a good claims reputation.</li></ol>"""),
      ("Tips for smooth claims", "<ul>"
       "<li><b>Answer the health questionnaire honestly</b>. Inaccurate information can lead to rejected claims.</li>"
       "<li><b>Keep the policy and member card</b> where your family can find them.</li>"
       "<li><b>Know the inpatient procedure</b>: when to contact the insurer and what documents are needed.</li>"
       "<li><b>Pay premiums on time</b> so the policy doesn't lapse.</li>"
       "<li><b>Review your policy</b> every few years as needs and healthcare costs change.</li></ul>"
       + TIP("calculate the BPJS Health contributions you already pay with the BPJS contribution calculator before deciding how much to budget for extra insurance.")),
      ("Conclusion", """<p>BPJS Health is a mandatory and relatively affordable foundation of health protection. Private insurance can complement it with better access and comfort, as long as you understand its limits, waiting periods, and exclusions. Choose based on your family's needs and your ability to pay premiums over the long term.</p>"""),
  ],
  faq=[("Do I need private insurance if I have BPJS?", "It isn't required. Private insurance helps if you want faster access, a wider choice of hospitals, or extra comfort, and the premium fits your budget."),
       ("Will premiums increase?", "Premiums generally rise with age and healthcare costs. Check the renewal terms in the policy."),
       ("What is unit-linked insurance?", "A product combining protection and investment. Understand its costs and risks; for many people, separating pure insurance and investing is more transparent.")])

A("merencanakan-dana-pensiun", slug="retirement-planning-indonesia",
  title="Retirement Planning in Indonesia: How Much You Need and How to Build It",
  h1="Planning Your Retirement Fund Early",
  desc="How to estimate retirement needs, the role of BPJS JHT and JP, DPLK and investment options, an example of monthly contributions, and tips for a calmer retirement.",
  lead="Retirement may feel far away, which is exactly why now is the best time to start. Time is a retirement fund's biggest asset.",
  body=[
      ("Why retirement needs planning", """<p>In retirement your salary stops but living costs continue, and healthcare costs tend to rise. Life expectancy is also longer, so retirement can last 20 years or more. Relying on your children or only on mandatory programs is often not enough.</p>
<p>A common rule of thumb is that retirement living costs are about <b>70–80% of your spending</b> before retirement, because some costs such as commuting and mortgage payments usually fall away.</p>"""),
      ("Sources of retirement income in Indonesia", """<ul><li><b>BPJS Employment JHT</b>: a savings balance withdrawn at retirement.</li>
<li><b>BPJS Employment JP</b>: a monthly pension if you have at least 15 years of contributions.</li>
<li><b>Employer pension programs</b>, if any, such as a DPPK or severance on retirement.</li>
<li><b>DPLK (financial institution pension fund)</b>: a voluntary pension program individuals can join, with certain tax benefits.</li>
<li><b>Personal investments</b>: mutual funds, government bonds, stocks, and property.</li></ul>
<p>Mandatory programs usually cover only part of your needs. The rest you build yourself.</p>"""),
      ("Example: estimating what you need", """<p>Say you're 25 and want to retire at 55 with living costs equal to <b>Rp7 million a month in today's money</b>, for about 25 years of retirement.</p>""" + T(["Step", "Calculation", "Result"], [
          ["Annual need (today's money)", "12 × Rp7 million", "Rp84 million"], ["Fund needed at retirement (today's money)", "Rp84 million × 25 years", "about Rp2.1 billion"],
          ["Equivalent 30 years from now (4% inflation)", "Rp7 million × 1.04³⁰ per month", "about Rp22.7 million a month"],
          ["=Monthly contribution at a 4% real return", "future value formula", "about Rp3.06 million (today's money, rising with inflation)"]]) + """
<p>That looks large, but part of it will be covered by JHT, JP, and employer programs. The result depends heavily on assumptions, so use it as a guide and review it every few years.</p>"""),
      ("Strategies for building a retirement fund", """<ul><li><b>Start as early as possible</b>, even small. Every 10-year delay can multiply the contribution needed.</li>
<li><b>Raise contributions every year</b> in line with salary increases.</li>
<li><b>Use growth assets</b> such as equity funds for the long term, then shift gradually to more stable instruments as retirement approaches.</li>
<li><b>Don't withdraw JHT</b> every time you change jobs unless necessary.</li>
<li><b>Pay off debts</b> before retiring, especially the mortgage.</li>
<li><b>Have health protection</b> so retirement savings aren't drained by medical bills.</li></ul>"""),
      ("Tips for a calmer retirement", "<ul>"
       "<li><b>Define a realistic retirement lifestyle</b> now.</li>"
       "<li><b>Keep a separate retirement account</b> so the money isn't used for other things.</li>"
       "<li><b>Review the plan every 2–3 years</b> and adjust for changes in income and needs.</li>"
       "<li><b>Consider passive income</b> or skills that can still earn after retirement.</li>"
       "<li><b>Beware of investment scams</b> targeting retirees with promises of high returns.</li></ul>"
       + TIP("simulate monthly contributions and annual increases in the investment calculator to estimate your fund at retirement age.")),
      ("Conclusion", """<p>A sufficient retirement fund comes from combining mandatory programs, employer programs, and personal investments started early. Estimate your needs with inflation in mind, contribute regularly, raise contributions as income grows, and review the plan periodically. The earlier you start, the lighter the load.</p>"""),
  ],
  faq=[("Are JHT and JP enough for retirement?", "For most people, no. They are a foundation; the rest needs to come from personal investing or voluntary pension programs."),
       ("When should I start?", "As soon as you start working. Even small contributions in your 20s can grow large thanks to compounding."),
       ("What is DPLK?", "A financial institution pension fund: a voluntary pension program managed by banks or insurers and supervised by OJK.")])

A("menyiapkan-dana-pendidikan-anak", slug="saving-for-childrens-education",
  title="How to Save for Your Child's Education: Estimate Costs and Choose Instruments",
  h1="How to Save for Your Child's Education",
  desc="A guide to education funds: estimating future costs with education inflation, an example monthly contribution, choosing instruments by time horizon, and tips to reach the target.",
  lead="Education costs rise every year. With early planning, school and university costs can be much easier to handle.",
  body=[
      ("Why start early", """<p>Education costs, especially enrollment fees and university tuition, tend to rise faster than general inflation. They also arrive at predictable times, which makes them ideal for regular investing.</p>
<p>The longer the horizon, the bigger the role of compounding and the smaller the monthly contribution needed.</p>"""),
      ("Example: estimating what you need", """<p>Suppose four years at the target university currently cost about <b>Rp100 million</b>, your child is 0, and will start university in 18 years. Assuming education costs rise 8% a year:</p>""" + T(["Step", "Calculation", "Result"], [
          ["Cost today", "", "Rp100 million"], ["Cost in 18 years", "Rp100 million × 1.08¹⁸", "about Rp400 million"],
          ["=Monthly contribution at an 8% annual return", "future value formula", "about Rp858,000 a month"]]) + """
<p>If you only start when your child is 8 (10 years before university), the contribution needed can be several times larger. The cost increase and return are just assumptions; get current fees from the school or university you have in mind.</p>"""),
      ("Choosing instruments by time horizon", T(["Time until needed", "Common choices", "Why"], [
          ["More than 10 years", "Equity funds, stocks, some balanced funds", "High growth potential, time to recover from drops"],
          ["5–10 years", "Balanced, fixed income funds, government bonds", "Balance of growth and stability"],
          ["Less than 5 years", "Government bonds, fixed income or money market funds, deposits", "Preserve value as the need approaches"],
          ["Less than 1 year", "Money market funds, deposits, savings", "Money must be safe and ready"]]) + """
<p>The principle: the closer the need, the larger the share in stable instruments. Shift gradually, not all at once at the last minute.</p>"""),
      ("Strategies to reach the target", """<ul><li><b>Separate funds by level</b>: primary, junior high, senior high, and university have different timelines.</li>
<li><b>Automate contributions</b> on payday to stay consistent.</li>
<li><b>Use extra income</b> such as bonuses and THR to speed up.</li>
<li><b>Protect the breadwinner</b> with pure life insurance so the plan continues if something happens.</li>
<li><b>Review every year</b>: adjust the target if fees rise faster than expected.</li></ul>"""),
      ("Tips for building an education fund", "<ul>"
       "<li><b>Research real costs</b> at target schools or universities, including enrollment fees and living costs if in another city.</li>"
       "<li><b>Don't use the education fund</b> for other purposes.</li>"
       "<li><b>Be careful with products promising high guaranteed returns.</b></li>"
       "<li><b>Involve your partner</b> in setting targets and choosing schools.</li>"
       "<li><b>Have a backup plan</b> such as scholarships or alternative universities.</li></ul>"
       + TIP("use the investment calculator to try several return scenarios and find a realistic monthly contribution.")),
      ("Conclusion", """<p>Your child's education fund can be prepared calmly when planned early: estimate future costs with education inflation, set a monthly contribution, choose instruments by time horizon, and move gradually to safer instruments as the need approaches. Consistency matters more than the size of early contributions.</p>"""),
  ],
  faq=[("Is a bank education savings account enough?", "It builds discipline, but returns are usually low. For the long term, combine it with investment instruments."),
       ("What if I have more than one child?", "Set separate targets and accounts for each child by age, then add up the monthly contributions."),
       ("Do I need education insurance?", "The most important thing is life cover for the breadwinner. Compare education insurance with pure life insurance plus separate investing.")])

A("beli-rumah-atau-sewa", slug="buy-or-rent-a-home-indonesia",
  title="Buy or Rent a Home in Indonesia? How to Compare the Costs and Decide",
  h1="Buy or Rent: Which Makes More Sense?",
  desc="A guide to comparing buying a home with a KPR versus renting: unrecoverable costs, the price-to-rent ratio, a 10-year example, and non-financial factors to consider.",
  lead="Buying isn't always better than renting, and vice versa. The answer depends on the numbers and your life plans.",
  body=[
      ("Not just installment vs. rent", """<p>Many people compare a KPR installment with rent and conclude &ldquo;buying is better because the house becomes mine&rdquo;. A fairer comparison looks at <b>unrecoverable costs</b> of each option:</p>
<ul><li><b>Renting</b>: the rent.</li>
<li><b>Buying</b>: mortgage interest, upfront costs (provision, notary, BPHTB), land and building tax, maintenance, insurance, and the lost investment return on the down payment.</li></ul>
<p>Principal repayments are not a cost, because they become your equity in the home. On the other hand, the home's value may rise over time, which benefits the buyer.</p>"""),
      ("A 10-year comparison", """<p>A house priced at <b>Rp600 million</b>, or rented for <b>Rp30 million a year</b> with rent rising 5% a year. If buying: 20% down, a Rp480 million KPR over 20 years at an average 9%.</p>""" + T(["First 10 years", "Rent", "Buy with KPR"], [
          ["Total rent", "about Rp377 million", "–"], ["Total KPR interest", "–", "about Rp379 million"],
          ["Upfront costs, property tax, maintenance (estimate)", "–", "tens of millions of rupiah"], ["Down payment not invested", "can be invested", "Rp120 million tied up in the house"],
          ["Remaining debt after 10 years", "–", "about Rp341 million"], ["Increase in home value", "–", "depends on location, can be significant"]]) + """
<p>In this example, the unrecoverable costs of renting and buying over 10 years are similar. What decides it is <b>home price growth</b> and the <b>investment return on the down payment</b> if you rent. Where prices rise quickly, buying tends to win; where prices are flat, renting and investing can come out ahead.</p>"""),
      ("The price-to-rent ratio", """<p>A quick check: divide the house price by a year's rent. In the example: Rp600 million ÷ Rp30 million = <b>20</b>.</p>
<ul><li><b>Low ratio</b> (for example below 15): prices are cheap relative to rent, so buying tends to be attractive.</li>
<li><b>High ratio</b> (for example above 20–25): prices are expensive relative to rent, so renting and investing can be more efficient.</li></ul>
<p>This ratio is only a starting tool. Interest rates, how long you plan to stay, and local price growth still matter.</p>"""),
      ("Non-financial factors", """<ul><li><b>How long you'll stay</b>: if you may move cities in 3–5 years, renting gives flexibility.</li>
<li><b>Income stability</b>: a KPR is a long commitment; unstable income makes it riskier.</li>
<li><b>Security and freedom</b>: your own home can be renovated as you like and gives a sense of ownership.</li>
<li><b>Family size</b>: space needs can change within a few years.</li></ul>"""),
      ("Tips for deciding", "<ul>"
       "<li><b>Use real numbers</b> for the area you want, not general estimates.</li>"
       "<li><b>If you rent, invest the difference</b>; without that, renting loses its advantage.</li>"
       "<li><b>If you buy, keep an emergency fund</b> after the down payment and upfront costs.</li>"
       "<li><b>Don't stretch</b> installments beyond 30–35% of income.</li>"
       "<li><b>Think of a home as a place to live</b>, not purely an investment.</li></ul>"
       + TIP("simulate installments and total interest with the mortgage calculator, then compare with total rent in the same area.")),
      ("Conclusion", """<p>Buying or renting isn't about right or wrong but about numbers and life plans. Compare the unrecoverable costs of each, account for home price growth and the investment potential of the down payment, then weigh flexibility and income stability. A good decision is one that keeps your finances healthy.</p>"""),
  ],
  faq=[("Is renting throwing money away?", "No. Owners also have unrecoverable costs such as interest, taxes, and maintenance. What matters is comparing total costs and outcomes."),
       ("House or apartment?", "It depends on location, space needs, and running costs. Apartments have regular service charges and ownership status to consider."),
       ("When is the best time to buy?", "When the down payment, upfront costs, and emergency fund are ready, income is stable, and you plan to stay for a long time.")])

A("mengatur-keuangan-freelancer", slug="personal-finance-for-freelancers",
  title="Managing Money as a Freelancer with Irregular Income",
  h1="How to Manage Your Finances as a Freelancer",
  desc="A personal finance guide for freelancers and people with irregular income: paying yourself a salary, buffer funds, tax, self-paid BPJS, separate accounts, and cash flow tips.",
  lead="Irregular income calls for a different way of managing money than a fixed salary. Here is a simple system you can apply.",
  body=[
      ("The financial challenges of freelancing", """<p>Freelancers, creators, consultants, and gig workers often have &ldquo;harvest&rdquo; months and &ldquo;lean&rdquo; months. There is no THR, no employer BPJS, and no automatic tax withholding. All of that becomes your responsibility. The key is a <b>system</b> that makes irregular income feel like a fixed salary.</p>"""),
      ("Three accounts and a salary for yourself", """<ol><li><b>Holding account</b>: all client payments land here.</li>
<li><b>Salary account</b>: each month, transfer a fixed amount from the holding account, as if paying yourself a salary. Base it on average income, for example the last 12 months minus a reserve.</li>
<li><b>Tax and obligations account</b>: set aside a percentage of every payment for tax, BPJS, and zakat.</li></ol>
<p>Surplus income in good months stays in the holding account as a <b>buffer</b> for lean months.</p>"""),
      ("Buffer and emergency funds", """<p>Because income is uncertain, freelancers need larger reserves than employees. A common benchmark is <b>6–12 months of expenses</b>. It can be layered:</p>""" + T(["Layer", "Purpose", "Where"], [
          ["Cash-flow buffer (2–3 months)", "Covers lean months", "Savings in the holding account"],
          ["Emergency fund (3–6 months)", "Illness, broken equipment, losing a big client", "Money market fund or separate savings"],
          ["Extra reserve", "Long transitions", "Laddered deposits"]])),
      ("Tax and social security", """<ul><li><b>Income tax</b>: fees from companies may have PPh 21 or PPh 23 withheld. If you run a business or independent profession, learn the bookkeeping options and applicable rates, including the 0.5% final rate on turnover for certain businesses under PP 55/2022. Keep withholding slips and income records for your annual return.</li>
<li><b>Self-paid BPJS Health</b>: register yourself and your family, and pay on time so coverage stays active.</li>
<li><b>BPJS Employment for non-wage earners (BPU)</b>: JKK and JKM at affordable rates, plus JHT as old-age savings.</li>
<li><b>Personal retirement fund</b>: with no employer program, build your own through regular investing or a DPLK.</li></ul>"""),
      ("Cash flow tips", "<ul>"
       "<li><b>Ask for a deposit</b> on large projects, for example 30–50% upfront.</li>"
       "<li><b>Use written contracts</b> covering scope, deadlines, and payment schedule.</li>"
       "<li><b>Send invoices on time</b> and follow up late payments.</li>"
       "<li><b>Diversify clients</b> so you don't depend on one source of income.</li>"
       "<li><b>Record all business income and expenses</b>, at least in a simple spreadsheet.</li>"
       "<li><b>Raise your rates periodically</b> in line with experience and inflation.</li></ul>"
       + TIP("keep the buffer layer in laddered deposits and calculate the net interest with the deposit calculator.")),
      ("Conclusion", """<p>Managing freelance finances means replacing the structure an employer usually provides with your own system: paying yourself a salary, building a larger buffer, setting aside tax and BPJS, and preparing a personal retirement fund. With a consistent system, irregular income no longer has to mean unstable finances.</p>"""),
  ],
  faq=[("What percentage should I set aside for tax?", "It depends on your income type and tax scheme. Calculate it under the applicable rules, then set aside a slightly larger percentage as a cushion."),
       ("Can freelancers get a mortgage?", "Yes, with bank statements, contracts, and tax records as proof of income. A well-documented income history helps a lot."),
       ("How do I decide my own salary?", "Take your average net income over the last 6–12 months, keep part of it as a reserve, and set the rest as a fixed monthly amount.")])
