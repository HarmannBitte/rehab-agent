# Anatomy issues checklist — systematic model coverage audit

> Created 2026-10-28. Purpose: list the human **anatomy issues that change
> body geometry, posture, movement, or internal structure** — the things the
> Rehab Agent digital twin may need to represent — so we can go through
> them systematically and record, for each one: *does a model exist, what
> kind, and can we use it?*
>
> **Scope:** musculoskeletal / structural / movement-relevant issues.
> Excluded: organ diseases, cancers, infections, metabolic diseases etc.
> *unless* they change geometry or movement (those cases are included via
> their structural effect, e.g. osteoporotic wedge vertebra).
>
> **Status legend**
> - `RESearched — models exist` = we have already checked (link to note)
> - `TO CHECK` = not yet researched
> - Later statuses as the audit proceeds: `MODEL EXISTS — adoptable`,
>   `MODEL EXISTS — research only`, `NO MODEL FOUND`, `OUT OF SCOPE`
>
> **Priority** = relevance to posture correction / twin accuracy
> (H = core, M = common or geometry-changing, L = rarer/specialist).

## A. Spine & trunk (SP)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| SP-01 | Scoliosis — adolescent idiopathic | Lateral spinal curvature + vertebral rotation, rib hump | H | RESearched — subject-specific OpenSim models exist (`research-detailed-anatomy-models.md` §2) |
| SP-02 | Scoliosis — congenital | Malformed vertebrae driving curvature | M | TO CHECK |
| SP-03 | Scoliosis — neuromuscular | Curvature from muscle imbalance/paralysis | M | TO CHECK |
| SP-04 | Scoliosis — adult degenerative | Asymmetric disc/facet degeneration curvature | M | TO CHECK |
| SP-05 | Hyperkyphosis / Scheuermann's kyphosis | Wedged thoracic vertebrae, rigid round back | H | TO CHECK |
| SP-06 | Postural kyphosis (flexible) | Habitual thoracic over-flexion, no bone change | H | TO CHECK |
| SP-07 | Lumbar hyperlordosis | Excess lumbar extension curve, anterior pelvic tilt coupling | H | TO CHECK |
| SP-08 | Flat back (lumbar hypolordosis) | Loss of lumbar curve | M | TO CHECK |
| SP-09 | Swayback posture | Pelvis shifted forward, thoracic back-sway | M | TO CHECK |
| SP-10 | Anterior pelvic tilt | Pelvis rotated forward; hip flexor/erector dominance | H | TO CHECK |
| SP-11 | Posterior pelvic tilt | Pelvis rotated backward; flat lumbar | M | TO CHECK |
| SP-12 | Pelvic obliquity (lateral tilt) | One side of pelvis higher; apparent leg-length difference | H | TO CHECK |
| SP-13 | Pelvic rotation asymmetry | Pelvis rotated in transverse plane | M | TO CHECK |
| SP-14 | Spondylolisthesis | Vertebra slipped forward on the one below | M | TO CHECK |
| SP-15 | Spondylolysis | Pars defect (stress fracture) in vertebra | L | TO CHECK |
| SP-16 | Spinal stenosis | Narrowed spinal canal/foramina | L | TO CHECK |
| SP-17 | Ankylosing spondylitis | Progressively fused/rigid spine | M | TO CHECK |
| SP-18 | Disc degeneration / herniation | Disc height loss, segment geometry change | M | TO CHECK |
| SP-19 | Osteoporotic vertebral wedge fracture | Wedged vertebral body → focal kyphosis | M | TO CHECK |
| SP-20 | Spine bending mechanics (general) | How curvature distributes across vertebrae | H | RESearched — articulated OpenSim spine models exist (§2 of anatomy note) |

## B. Head, neck & jaw (HN)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| HN-01 | Forward head posture | Head translated forward of trunk line | H | TO CHECK |
| HN-02 | Loss of cervical lordosis ("military neck") | Straightened cervical curve | M | TO CHECK |
| HN-03 | Cervical kyphosis | Reversed cervical curve | M | TO CHECK |
| HN-04 | Torticollis (congenital muscular / spasmodic) | Sternocleidomastoid shortening/spasm, head tilt+rotation | M | TO CHECK |
| HN-05 | TMJ disorder / jaw misalignment | Jaw joint mechanics, bite asymmetry | L | TO CHECK |
| HN-06 | Cranial asymmetry (plagiocephaly) | Skull shape asymmetry | L | TO CHECK |

## C. Shoulder girdle (SH)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| SH-01 | Rounded shoulders | Protracted/ internally rotated shoulder girdle posture | H | TO CHECK |
| SH-02 | Scapular winging | Medial scapular border lifts off rib cage (serratus/long thoracic) | M | TO CHECK |
| SH-03 | Scapular dyskinesis | Abnormal scapular motion pattern in arm movement | M | TO CHECK |
| SH-04 | Shoulder impingement anatomy | Acromion shape / subacromial space narrowing | M | TO CHECK |
| SH-05 | Rotator cuff tear + fatty infiltration | Tendon tear, muscle atrophy/fatty degeneration | M | TO CHECK |
| SH-06 | Adhesive capsulitis (frozen shoulder) | Capsular contracture, severe range loss | M | TO CHECK |
| SH-07 | Shoulder instability | Laxity / labral anatomy, dislocation history | L | TO CHECK |
| SH-08 | Clavicle malunion / deformity | Shortened/angulated clavicle after fracture | L | TO CHECK |
| SH-09 | Thoracic outlet compression anatomy | Narrowed scalene/costoclavicular space | L | TO CHECK |

## D. Arm, elbow, wrist & hand (UL)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| UL-01 | Cubitus valgus / varus | Elbow carrying-angle deformity | L | TO CHECK |
| UL-02 | Elbow flexion contracture | Fixed loss of extension | M | TO CHECK |
| UL-03 | Madelung deformity (wrist) | Distal radius growth deformity | L | TO CHECK |
| UL-04 | Dupuytren's contracture | Palmar fascia cords, finger flexion deformity | L | TO CHECK |
| UL-05 | Rheumatoid hand deformities | Swan-neck / boutonnière / ulnar drift | L | TO CHECK |

## E. Hip & pelvis (HP)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| HP-01 | Developmental hip dysplasia | Shallow acetabulum, femoral head coverage loss | M | TO CHECK |
| HP-02 | Femoroacetabular impingement — cam | Aspherical femoral head-neck junction | M | TO CHECK |
| HP-03 | Femoroacetabular impingement — pincer | Acetabular over-coverage | M | TO CHECK |
| HP-04 | Coxa vara / coxa valga | Femoral neck-shaft angle decreased / increased | M | TO CHECK |
| HP-05 | Femoral anteversion | Femoral neck twisted forward → in-toeing | H | TO CHECK |
| HP-06 | Femoral retroversion | Femoral neck twisted backward → out-toeing | M | TO CHECK |
| HP-07 | Hip osteoarthritis | Joint space loss, osteophytes, deformity | H | TO CHECK |
| HP-08 | Avascular necrosis of femoral head | Femoral head collapse | L | TO CHECK |
| HP-09 | Total hip replacement | Prosthetic joint geometry, leg-length change | M | TO CHECK |
| HP-10 | Gluteal insufficiency / Trendelenburg | Hip abductor weakness → pelvic drop in gait | H | TO CHECK |

## F. Knee & leg alignment (KN)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| KN-01 | Genu valgum (knock knees) | Valgus knee alignment | H | TO CHECK |
| KN-02 | Genu varum (bow legs) | Varus knee alignment | H | TO CHECK |
| KN-03 | Genu recurvatum | Knee hyperextension | M | TO CHECK |
| KN-04 | Patella alta / baja | Patella abnormally high / low | L | TO CHECK |
| KN-05 | Patellar maltracking / instability | Patella tracks laterally, dislocation risk | M | TO CHECK |
| KN-06 | Tibial torsion (internal/external) | Shin bone twisted along its axis | M | TO CHECK |
| KN-07 | Knee osteoarthritis | Compartment joint-space loss → progressive varus/valgus | H | TO CHECK |
| KN-08 | Ligament laxity / ACL deficiency | Joint instability | M | TO CHECK |
| KN-09 | Meniscal injury/deficiency | Load-distribution anatomy changed | L | TO CHECK |
| KN-10 | Osgood-Schlatter (adolescent) | Tibial tubercle apophysitis/bump | L | TO CHECK |
| KN-11 | Knee flexion contracture | Fixed loss of extension (common post-stroke/arthritic) | M | TO CHECK |
| KN-12 | Total knee replacement | Prosthetic joint geometry/alignment | M | TO CHECK |

## G. Foot & ankle (FT)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| FT-01 | Pes planus — flexible flat foot | Arch collapses under load, recovers unloaded | H | RESearched — FE + kinematic models exist (§1 of anatomy note) |
| FT-02 | Adult-acquired flat foot (posterior tibial tendon dysfunction) | Progressive arch collapse + hindfoot valgus | M | TO CHECK |
| FT-03 | Pes cavus (high arch) | Abnormally high, rigid arch | M | TO CHECK |
| FT-04 | Dynamic overpronation | Excess arch collapse/eversion in gait | H | TO CHECK |
| FT-05 | Oversupination | Lateral loading, rigid high-arch gait | L | TO CHECK |
| FT-06 | Hallux valgus (bunion) | Big-toe lateral deviation + 1st metatarsal shift | M | TO CHECK |
| FT-07 | Hallux rigidus | 1st MTP joint arthritis/stiffness | L | TO CHECK |
| FT-08 | Hammer / claw / mallet toes | Toe joint deformities | L | TO CHECK |
| FT-09 | Plantar fasciitis / fascia thickening | Plantar fascia degeneration/thickening | M | TO CHECK |
| FT-10 | Achilles tendinopathy / Haglund deformity | Tendon thickening / heel bone prominence | L | TO CHECK |
| FT-11 | Clubfoot (talipes equinovarus) | Congenital inward/downward foot deformity | M | TO CHECK |
| FT-12 | Tarsal coalition | Abnormal bone/cartilage bridge between tarsals | L | TO CHECK |
| FT-13 | Metatarsus adductus | Forefoot deviated inward (paediatric) | L | TO CHECK |
| FT-14 | Chronic ankle instability | Ligament laxity, recurrent giving way | M | TO CHECK |
| FT-15 | Equinus (gastrocnemius/soleus tightness) | Limited ankle dorsiflexion | M | TO CHECK |
| FT-16 | Arch height (general mechanics) | Dynamic arch rise/collapse in gait | H | RESearched — multi-segment + synergy foot models exist (§1 of anatomy note) |

## H. Whole-body alignment, proportions & composition (WB)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| WB-01 | Leg-length discrepancy — structural | True bone length difference | H | TO CHECK |
| WB-02 | Leg-length discrepancy — functional | Apparent difference from pelvis/foot posture | M | TO CHECK |
| WB-03 | Obesity / regional fat distribution | Fat mass amount + depot pattern | H | RESearched — see `fat-distribution/` folder |
| WB-04 | Lipedema | Symmetrical painful leg fat deposition, spares feet | M | TO CHECK |
| WB-05 | Lipodystrophy | Regional fat loss/redistribution | L | TO CHECK |
| WB-06 | Left–right muscle asymmetry | Side-to-side muscle size/strength difference | H | TO CHECK |
| WB-07 | Limb amputation (upper/lower) | Missing limb segment; prosthesis interface | M | TO CHECK |
| WB-08 | Congenital limb deficiency | Partially formed limb | L | TO CHECK |
| WB-09 | Skeletal dysplasia / achondroplasia | Short-limb body proportions | L | TO CHECK |
| WB-10 | Marfan habitus | Tall, long-limb proportions, chest deformity link | L | TO CHECK |
| WB-11 | Pregnancy-related anatomical change | Centre-of-mass shift, lordosis, abdominal wall change | M | TO CHECK |
| WB-12 | Ageing posture change | Kyphosis increase, height loss, sarcopenia coupling | M | TO CHECK |

## I. Muscle, tendon & soft tissue (MS)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| MS-01 | Sarcopenia | Age-related muscle mass/quality loss (incl. fatty infiltration) | H | TO CHECK |
| MS-02 | Muscle atrophy (disuse/neurogenic) | Local muscle volume loss | H | TO CHECK |
| MS-03 | Muscle fatty infiltration | Fat within muscle (measurable as MRI fat fraction) | H | TO CHECK (fat methods in `fat-distribution/measurement-notes.md`) |
| MS-04 | Muscle/tendon contracture (general) | Fixed shortening limiting joint range | H | TO CHECK |
| MS-05 | Upper crossed syndrome (Janda) | Tight pectorals/upper traps vs weak deep neck flexors/scapular muscles | M | TO CHECK |
| MS-06 | Lower crossed syndrome (Janda) | Tight hip flexors/erectors vs weak abdominals/gluteals | M | TO CHECK |
| MS-07 | Joint hypermobility / Ehlers-Danlos | Ligament laxity, excessive joint range, instability | M | TO CHECK |
| MS-08 | Diastasis recti | Separated rectus abdominis along linea alba | M | TO CHECK |
| MS-09 | Lymphedema / chronic edema | Regional limb volume increase (fluid) | L | TO CHECK |
| MS-10 | Tendinopathy (general mechanics) | Tendon thickening/stiffness change | L | TO CHECK |

## J. Bone & joint — general (BJ)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| BJ-01 | Osteoporosis / low bone mineral density | Bone mass/strength loss (DXA-measurable) | M | TO CHECK |
| BJ-02 | Osteoarthritis (non hip/knee joints) | Joint space loss, deformity (shoulder, ankle, spine facets, hands) | M | TO CHECK |
| BJ-03 | Rheumatoid arthritis deformity pattern | Inflammatory joint destruction pattern | L | TO CHECK |
| BJ-04 | Fracture malunion | Bone healed in deformed position | M | TO CHECK |
| BJ-05 | Other joint replacements (shoulder, ankle) | Prosthetic joint geometry | L | TO CHECK |
| BJ-06 | Rickets / osteomalacia | Softened bone → bowing deformities | L | TO CHECK |

## K. Neuromotor conditions (movement presentation) (NM)

> Not "anatomy defects" themselves, but conditions whose *anatomical
> presentation* (posture, alignment, muscle bulk) the twin will encounter.

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| NM-01 | Cerebral palsy — crouch gait | Persistent hip/knee flexion gait pattern | M | TO CHECK |
| NM-02 | Cerebral palsy — spastic equinus / patterns | Spasticity-driven foot/limb postures, contractures | M | TO CHECK |
| NM-03 | Stroke hemiparesis posture | One-sided weakness/spasticity, asymmetric posture | H | TO CHECK |
| NM-04 | Parkinsonian stooped posture / camptocormia | Trunk flexion posture, rigidity pattern | M | TO CHECK |
| NM-05 | Foot drop (peroneal nerve / L5) | Dorsiflexor failure, steppage gait | M | TO CHECK |
| NM-06 | Muscular dystrophy posture | Progressive weakness → lordosis, pseudohypertrophy | L | TO CHECK |
| NM-07 | Spinal muscular atrophy | Proximal weakness postures | L | TO CHECK |
| NM-08 | Multiple sclerosis gait/posture | Spasticity + weakness + ataxia combination | L | TO CHECK |
| NM-09 | Dystonia (incl. cervical) | Involuntary sustained muscle contractions → abnormal postures | L | TO CHECK |
| NM-10 | Charcot (neuropathic) foot | Joint/bone collapse from neuropathy | L | TO CHECK |
| NM-11 | Spasticity / hypertonia (general) | Velocity-dependent muscle overactivity | H | TO CHECK |
| NM-12 | Hypotonia (general) | Low muscle tone, postural collapse tendency | M | TO CHECK |

## L. Chest, rib cage, breathing & abdominal wall (RA)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| RA-01 | Breathing pattern disorder (thoracic-dominant) | Upper-chest dominant ventilation, diaphragm under-recruited | H | RESearched — tracking + metrics in `research-breathing-tracking.md` |
| RA-02 | Paradoxical breathing / thoracoabdominal asynchrony | Abdomen moves inward on inhalation etc. | M | RESearched — phase-angle methods (§2–3 of breathing note) |
| RA-03 | Diaphragm paralysis / dysfunction | Elevated, weak or paradoxical hemidiaphragm | M | RESearched — ultrasound measures (excursion/thickening) in breathing note |
| RA-04 | Pectus excavatum | Sternum sunken inward | M | TO CHECK |
| RA-05 | Pectus carinatum | Sternum protruding outward | L | TO CHECK |
| RA-06 | Barrel chest (COPD hyperinflation) | Increased AP chest diameter, flattened diaphragm | M | TO CHECK |
| RA-07 | Rib flare | Lower ribs protrude outward (often with lordosis/diaphragm position) | M | TO CHECK |
| RA-08 | Rib hump (scoliosis-linked) | Rib cage rotational deformity | M | TO CHECK (links SP-01) |
| RA-09 | Abdominal wall hernia | Wall defect with protrusion | L | TO CHECK |
| RA-10 | Rib cage expansion mechanics (general) | Pump/bucket-handle expansion, diaphragm coupling | H | RESearched — rib/diaphragm models in anatomy note §3 + breathing note |

## Count & working order

**128 issues** (SP 20, HN 6, SH 9, UL 5, HP 10, KN 12, FT 16, WB 12,
MS 10, BJ 6, NM 12, RA 10).

Already researched (9): SP-01, SP-20, FT-01, FT-16, WB-03, RA-01, RA-02,
RA-03, RA-10 (and MS-03 partially, via the fat-measurement notes).

Suggested audit order (by twin impact):
1. **Spine/trunk remainder** (SP-05…SP-19) — posture is the core claim.
2. **Hip/knee/foot alignment chain** (HP, KN, FT remainder) — gait and
   squat-class movement claims depend on it.
3. **Shoulder girdle** (SH) — upper-body correction claims.
4. **Whole-body + muscle** (WB, MS) — asymmetry, atrophy, hypermobility.
5. **Chest/abdominal** (RA remainder) + **head/neck** (HN).
6. **Neuromotor + bone/joint + arm/hand** (NM, BJ, UL) — population
   coverage and edge cases.

For each issue, the audit records: model exists? (paper / dataset /
software / OpenSim-FE-avatar), open or closed, input it needs, accuracy
evidence, and a twin decision (adopt / adapt / visualise-only / exclude).
Findings go in follow-up research notes per region, linked from here.
