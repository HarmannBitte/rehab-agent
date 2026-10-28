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

## M. Niche & rare additions (added 2026-10-28)

> The main list (A–L) covers common and moderately common issues. This
> section adds the **niche layer**: rare, congenital, paediatric,
> post-surgical and syndrome-associated conditions that still change body
> geometry, posture, or movement. IDs continue each region's numbering so
> references stay stable. Deliberately still excluded: pain-only
> conditions with no structural/movement signature (e.g. fibromyalgia,
> Morton's neuroma), transient injuries with normal healing, and internal
> organ disease without a geometry/movement effect.

### Spine niche (SP, continued)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| SP-21 | Klippel-Feil syndrome | Congenitally fused cervical vertebrae, short neck, low motion | L | TO CHECK |
| SP-22 | Hemivertebra / congenital vertebral malformation | Half-formed vertebra → congenital scoliosis/kyphosis driver | L | TO CHECK |
| SP-23 | Lumbosacral transitional vertebra (sacralisation/lumbarisation, Bertolotti) | Extra/fused lumbosacral segment alters load transfer | L | TO CHECK |
| SP-24 | Spina bifida (posterior arch defect) | Missing vertebral arch; neurological level-dependent posture | L | TO CHECK |
| SP-25 | DISH (diffuse idiopathic skeletal hyperostosis) | Flowing spinal ossification → stiff spine | L | TO CHECK |
| SP-26 | Atlantoaxial instability (e.g. Down syndrome) | C1–C2 laxity, head/neck positioning risk | L | TO CHECK |
| SP-27 | Gibbus deformity | Sharp angular kyphosis (e.g. post-infectious Pott disease) | L | TO CHECK |
| SP-28 | Thoracic insufficiency syndrome | Fused ribs/spine — chest cannot expand for lung growth | L | TO CHECK |
| SP-29 | Basilar invagination / cranial settling | Skull base settling onto cervical spine | L | TO CHECK |
| SP-30 | OPLL (ossification of posterior longitudinal ligament) | Ossified ligament stiffens/narrows cervical canal | L | TO CHECK |

### Head/neck niche (HN, continued)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| HN-07 | Cervical rib | Extra rib above 1st rib (thoracic-outlet link, SH-09) | L | TO CHECK |
| HN-08 | Hemifacial microsomia / craniofacial asymmetry | One side of face/jaw underdeveloped | L | TO CHECK |
| HN-09 | Retrognathia / micrognathia / prognathism | Jaw size/position discrepancies | L | TO CHECK |
| HN-10 | Ocular torticollis | Compensatory head tilt from eye-muscle imbalance | L | TO CHECK |
| HN-11 | Webbed neck (pterygium colli, e.g. Turner/Noonan) | Neck skin webbing, low hairline, posture appearance | L | TO CHECK |
| HN-12 | TMJ ankylosis | Fused jaw joint, severe opening restriction | L | TO CHECK |

### Shoulder niche (SH, continued)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| SH-10 | Sprengel deformity | Congenitally high, small scapula | L | TO CHECK |
| SH-11 | Poland syndrome | Absent pectoralis major (+ hand differences), chest asymmetry | L | TO CHECK |
| SH-12 | Snapping scapula syndrome | Scapulothoracic crepitus/abnormal tracking | L | TO CHECK |
| SH-13 | Obstetric brachial plexus palsy (Erb's) posture | "Waiter's tip" arm posture, growth asymmetry | L | TO CHECK |
| SH-14 | Glenoid dysplasia / retroversion | Shallow/misoriented shoulder socket | L | TO CHECK |
| SH-15 | Os acromiale / acromial variants | Unfused acromial ossification centre altering deltoid mechanics | L | TO CHECK |

### Arm/hand niche (UL, continued)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| UL-06 | Congenital radioulnar synostosis | Radius/ulna fused — forearm rotation fixed | L | TO CHECK |
| UL-07 | Radial longitudinal deficiency (radial club hand) | Partial/absent radius, radial hand deviation | L | TO CHECK |
| UL-08 | Camptodactyly / clinodactyly | Fixed finger flexion / lateral finger curvature | L | TO CHECK |
| UL-09 | Syndactyly / polydactyly (hand) | Fused or extra digits — hand shape/grip | L | TO CHECK |
| UL-10 | Volkmann ischaemic contracture | Forearm muscle fibrosis → claw-like contracture | L | TO CHECK |
| UL-11 | Trigger finger (stenosing tenosynovitis) | Tendon catching, functional grip loss | L | TO CHECK |

### Hip niche (HP, continued)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| HP-11 | Legg-Calvé-Perthes disease | Childhood femoral-head necrosis → deformed head/hip | L | TO CHECK |
| HP-12 | Slipped capital femoral epiphysis (SCFE) | Growth-plate slip → hip deformity, leg rotation change | L | TO CHECK |
| HP-13 | Protrusio acetabuli | Socket protrudes into pelvis, deep hip | L | TO CHECK |
| HP-14 | Acetabular retroversion | Socket opening faces backward → impingement pattern | L | TO CHECK |
| HP-15 | Sacroiliac joint asymmetry/dysfunction | Pelvic ring asymmetry perception/mechanics | M | TO CHECK |
| HP-16 | Proximal femoral focal deficiency | Underdeveloped proximal femur → major leg-length difference | L | TO CHECK |

### Knee/leg niche (KN, continued)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| KN-13 | Blount disease (tibia vara) | Growth disorder bowing the proximal tibia (infantile/adolescent) | L | TO CHECK |
| KN-14 | Discoid meniscus | Disc-shaped (not C-shaped) meniscus, snapping knee | L | TO CHECK |
| KN-15 | Nail-patella syndrome | Small/absent patellae + elbow and iliac anomalies | L | TO CHECK |
| KN-16 | Congenital knee dislocation | Hyperextended/dislocated knee at birth | L | TO CHECK |
| KN-17 | Fibular hemimelia | Partial/absent fibula → leg-length and foot deformity | L | TO CHECK |
| KN-18 | Bipartite patella (variant) | Patella in two unfused parts — usually incidental | L | TO CHECK |

### Foot niche (FT, continued)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| FT-17 | Congenital vertical talus | "Rocker-bottom" rigid flat foot | L | TO CHECK |
| FT-18 | Cavovarus foot | High arch + hindfoot varus (often Charcot-Marie-Tooth, NM-13) | M | TO CHECK |
| FT-19 | Skewfoot (serpentine foot) | Combined forefoot adduction + hindfoot valgus Z-deformity | L | TO CHECK |
| FT-20 | Brachymetatarsia | Abnormally short metatarsal (usually 4th toe) | L | TO CHECK |
| FT-21 | Accessory navicular syndrome | Extra navicular ossicle altering tibialis posterior mechanics | L | TO CHECK |
| FT-22 | Freiberg infraction | Flattened metatarsal head (osteochondrosis) | L | TO CHECK |
| FT-23 | Toe polydactyly / syndactyly / macrodactyly | Extra, fused, or enlarged toes | L | TO CHECK |
| FT-24 | Calcaneovalgus foot | Newborn foot bent up/outward (usually flexible) | L | TO CHECK |
| FT-25 | Köhler / Sever osteochondroses | Paediatric navicular/heel growth-plate conditions | L | TO CHECK |

### Whole-body niche (WB, continued)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| WB-13 | Hemihypertrophy / hemihypotrophy | One body side over- or under-grown | L | TO CHECK |
| WB-14 | Segmental overgrowth (Proteus, Klippel-Trénaunay) | Progressive asymmetric limb overgrowth (+ vascular in KTS) | L | TO CHECK |
| WB-15 | Acromegaly / gigantism proportions | Enlarged jaw, hands, feet; altered proportions | L | TO CHECK |
| WB-16 | Multiple hereditary exostoses | Multiple bone outgrowths deforming limbs/joints | L | TO CHECK |
| WB-17 | Neurofibromatosis type 1 skeletal signs | Tibial bowing/pseudoarthrosis, scoliosis link | L | TO CHECK |
| WB-18 | Cachexia (severe wasting) | Extreme muscle/fat loss changing body shape | L | TO CHECK |
| WB-19 | Burn / scar contractures | Skin/fascia shortening restricting joint motion regionally | M | TO CHECK |

### Muscle/soft-tissue niche (MS, continued)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| MS-11 | Muscle rupture with retraction (e.g. "Popeye" biceps) | Muscle belly displaced/deformed after tendon rupture | L | TO CHECK |
| MS-12 | Muscle hernia | Muscle bulging through fascial defect | L | TO CHECK |
| MS-13 | Heterotopic ossification / myositis ossificans | Bone forming inside muscle → motion block | L | TO CHECK |
| MS-14 | Myotonic disorders (stiffness) | Delayed muscle relaxation altering movement pattern | L | TO CHECK |
| MS-15 | Chronic exertional compartment syndrome | Exercise-induced compartment pressure (functional, low geometry signal) | L | TO CHECK |

### Bone/joint niche (BJ, continued)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| BJ-07 | Osteogenesis imperfecta | Brittle bones → recurrent fractures, bowing, short stature | L | TO CHECK |
| BJ-08 | Paget disease of bone | Enlarged, deformed, weak bone (e.g. bowed tibia, skull) | L | TO CHECK |
| BJ-09 | Fibrous dysplasia | Fibrous bone replacement → deformity (e.g. shepherd's-crook femur) | L | TO CHECK |
| BJ-10 | Osteopetrosis | Over-dense brittle bone, deformity/fracture pattern | L | TO CHECK |
| BJ-11 | Limb-salvage / tumour resection reconstruction | Resected bone with endoprosthesis — non-standard anatomy | L | TO CHECK |

### Neuromotor niche (NM, continued)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| NM-13 | Charcot-Marie-Tooth disease | Progressive distal wasting → cavovarus feet, hand wasting | M | TO CHECK |
| NM-14 | Friedreich / hereditary ataxias | Progressive scoliosis + pes cavus + gait ataxia pattern | L | TO CHECK |
| NM-15 | Post-polio residual deformity | Asymmetric atrophy, limb shortening, joint deformity | L | TO CHECK |

### Chest/breathing niche (RA, continued)

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| RA-11 | Diaphragmatic eventration / unilateral elevation | Abnormally high, thin diaphragm dome | L | TO CHECK |
| RA-12 | Post-surgical chest-wall deformity | Thoracotomy/mastectomy asymmetry affecting posture/breathing | L | TO CHECK |

### Systemic congenital (NC) — cross-cutting

| ID | Issue | What changes anatomically | Priority | Status |
|---|---|---|---|---|
| NC-01 | Arthrogryposis multiplex congenita | Multiple congenital joint contractures (links UL/MS regions) | L | TO CHECK |
| NC-02 | Down syndrome musculoskeletal pattern | Hypotonia + ligament laxity + atlantoaxial risk (SP-26) + flat feet | M | TO CHECK |
| NC-03 | Cerebral-palsy-associated skeletal deformity set | Hip displacement, torsional deformity, scoliosis cluster (links NM-01/02) | M | TO CHECK |

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
