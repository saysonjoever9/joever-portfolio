from pathlib import Path

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Joever L. Sayson | Computer Engineer Portfolio</title>
<meta name="description" content="Portfolio of Joever L. Sayson — Computer Engineering Graduate, researcher, AI/ML and computer vision developer.">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');

:root{
  --bg:#070b12; --bg2:#0c1220; --card:rgba(16,24,39,.72);
  --text:#eef4ff; --muted:#9aa9bd; --line:rgba(148,163,184,.15);
  --accent:#61dafb; --accent2:#8b5cf6; --good:#4ade80;
  --shadow:0 25px 80px rgba(0,0,0,.35);
  --engr-blue:#2563eb; --engr-cyan:#22d3ee;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{
  font-family:Inter,system-ui,sans-serif;color:var(--text);background:var(--bg);
  overflow-x:hidden;position:relative;
}

/* ============ ANIMATED BACKGROUND LAYERS ============ */

/* Canvas particle network */
#particleCanvas{
  position:fixed;inset:0;z-index:0;pointer-events:none;opacity:.55;
}

/* Animated gradient orbs */
.bg-orbs{
  position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden;
}
.orb{
  position:absolute;border-radius:50%;filter:blur(80px);opacity:.35;
  will-change:transform;
}
.orb1{
  width:520px;height:520px;background:radial-gradient(circle,#61dafb,transparent 70%);
  top:-160px;left:-120px;animation:orbFloat1 22s ease-in-out infinite;
}
.orb2{
  width:600px;height:600px;background:radial-gradient(circle,#8b5cf6,transparent 70%);
  top:20%;right:-200px;animation:orbFloat2 28s ease-in-out infinite;
}
.orb3{
  width:450px;height:450px;background:radial-gradient(circle,#22d3ee,transparent 70%);
  bottom:-150px;left:30%;animation:orbFloat3 25s ease-in-out infinite;
}
.orb4{
  width:380px;height:380px;background:radial-gradient(circle,#4ade80,transparent 70%);
  top:60%;left:-100px;opacity:.2;animation:orbFloat2 32s ease-in-out infinite reverse;
}
@keyframes orbFloat1{
  0%,100%{transform:translate(0,0) scale(1)}
  33%{transform:translate(120px,80px) scale(1.1)}
  66%{transform:translate(60px,160px) scale(.95)}
}
@keyframes orbFloat2{
  0%,100%{transform:translate(0,0) scale(1)}
  33%{transform:translate(-140px,100px) scale(1.08)}
  66%{transform:translate(-80px,-60px) scale(.92)}
}
@keyframes orbFloat3{
  0%,100%{transform:translate(0,0) scale(1)}
  50%{transform:translate(100px,-120px) scale(1.15)}
}

/* Grid pattern with subtle pulse */
.grid-overlay{
  position:fixed;inset:0;z-index:0;pointer-events:none;
  background-image:
    linear-gradient(rgba(97,218,251,.05) 1px,transparent 1px),
    linear-gradient(90deg,rgba(97,218,251,.05) 1px,transparent 1px);
  background-size:55px 55px;
  mask-image:radial-gradient(ellipse at 50% 0%,#000 0%,transparent 75%);
  -webkit-mask-image:radial-gradient(ellipse at 50% 0%,#000 0%,transparent 75%);
  animation:gridPulse 8s ease-in-out infinite;
}
@keyframes gridPulse{
  0%,100%{opacity:.6}
  50%{opacity:1}
}

/* Circuit traces overlay */
.circuit-overlay{
  position:fixed;inset:0;z-index:0;pointer-events:none;opacity:.08;
  background-image:
    radial-gradient(circle at 20% 30%,rgba(97,218,251,.6) 1px,transparent 2px),
    radial-gradient(circle at 80% 70%,rgba(139,92,246,.6) 1px,transparent 2px),
    radial-gradient(circle at 40% 80%,rgba(34,211,238,.6) 1px,transparent 2px),
    radial-gradient(circle at 60% 20%,rgba(74,222,128,.6) 1px,transparent 2px);
  background-size:400px 400px;
  animation:circuitDrift 40s linear infinite;
}
@keyframes circuitDrift{
  from{background-position:0 0}
  to{background-position:400px 400px}
}

/* Twinkling stars */
.stars{
  position:fixed;inset:0;z-index:0;pointer-events:none;
}
.star{
  position:absolute;width:2px;height:2px;background:#fff;border-radius:50%;
  animation:twinkle 3s ease-in-out infinite;
}
@keyframes twinkle{
  0%,100%{opacity:.2;transform:scale(.8)}
  50%{opacity:1;transform:scale(1.4)}
}

/* Shooting star */
.shooting-star{
  position:fixed;width:120px;height:2px;z-index:0;pointer-events:none;
  background:linear-gradient(90deg,transparent,#61dafb,transparent);
  filter:drop-shadow(0 0 6px #61dafb);
  opacity:0;animation:shoot 8s linear infinite;
}
.shooting-star:nth-child(1){top:15%;left:-200px;animation-delay:2s}
.shooting-star:nth-child(2){top:45%;left:-200px;animation-delay:6s}
.shooting-star:nth-child(3){top:75%;left:-200px;animation-delay:11s}
@keyframes shoot{
  0%{opacity:0;transform:translateX(0) rotate(-15deg)}
  5%{opacity:1}
  15%{opacity:1;transform:translateX(120vw) rotate(-15deg)}
  16%,100%{opacity:0}
}

/* Content sits above background */
nav, main, footer, .ai, .ai-panel{position:relative;z-index:1}

a{color:inherit;text-decoration:none}
.container{width:min(1120px,92%);margin:auto}
nav{
  position:fixed;top:0;left:0;width:100%;z-index:50;
  background:rgba(7,11,18,.68);backdrop-filter:blur(16px);
  border-bottom:1px solid var(--line)
}
.nav-inner{height:72px;display:flex;align-items:center;justify-content:space-between}
.logo{font-family:"Space Grotesk";font-size:1.5rem;font-weight:700;display:flex;align-items:center;gap:8px}
.logo-icon{
  width:38px;height:38px;background:linear-gradient(135deg,var(--accent),var(--accent2));
  border-radius:10px;display:flex;align-items:center;justify-content:center;
  font-size:1.2rem;color:#061018;box-shadow:0 0 24px rgba(97,218,251,.3);transition:.3s;
}
.logo:hover .logo-icon{transform:rotate(-10deg) scale(1.08);box-shadow:0 0 36px rgba(97,218,251,.5)}
.logo span{color:var(--accent)}
.logo-sub{font-size:.55rem;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);font-weight:600;font-family:Inter;line-height:1;margin-left:2px}
.nav-links{display:flex;gap:22px;color:var(--muted);font-size:.85rem;font-weight:500;align-items:center}
.nav-links a{transition:.25s;display:flex;align-items:center;gap:5px}
.nav-links a i{font-size:.8rem;opacity:.7}
.nav-links a:hover{color:var(--accent)}
.nav-links a:hover i{opacity:1}
.menu{display:none;background:none;border:0;color:white;font-size:1.5rem;cursor:pointer}

.hero{min-height:100vh;display:grid;place-items:center;padding:120px 0 70px;position:relative}
.hero-grid{display:grid;grid-template-columns:1.15fr .85fr;gap:70px;align-items:center}
.badge{
  display:inline-flex;align-items:center;gap:8px;padding:8px 14px;border:1px solid var(--line);
  background:rgba(255,255,255,.035);border-radius:999px;color:#c9d5e6;font-size:.8rem;margin-bottom:22px;font-weight:500
}
.badge i{color:var(--accent);font-size:.85rem}
.dot{width:8px;height:8px;border-radius:50%;background:var(--good);box-shadow:0 0 15px var(--good);animation:pulse 1.7s infinite}
@keyframes pulse{50%{transform:scale(1.5);opacity:.5}}
h1{font-family:"Space Grotesk";font-size:clamp(3rem,7vw,6.5rem);line-height:.92;letter-spacing:-.065em}
.gradient{background:linear-gradient(100deg,var(--accent),#fff 43%,#a78bfa);-webkit-background-clip:text;background-clip:text;color:transparent}
.engr-tag{
  display:inline-block;font-size:.7rem;letter-spacing:.25em;text-transform:uppercase;
  color:var(--engr-cyan);border:1px solid rgba(34,211,238,.25);padding:4px 12px;border-radius:4px;
  margin-bottom:16px;font-weight:600;background:rgba(34,211,238,.04)
}
.hero p{color:var(--muted);font-size:1.08rem;line-height:1.8;max-width:680px;margin:25px 0}
.buttons{display:flex;gap:13px;flex-wrap:wrap}
.btn{padding:13px 22px;border-radius:12px;border:1px solid var(--line);font-weight:600;font-size:.9rem;transition:.25s;display:inline-flex;align-items:center;gap:8px}
.btn i{font-size:.85rem}
.btn.primary{background:linear-gradient(135deg,var(--accent),#3b82f6);color:#061018;border:0}
.btn:hover{transform:translateY(-3px);box-shadow:0 12px 30px rgba(97,218,251,.12)}
.hero-card{
  min-height:460px;border:1px solid var(--line);background:linear-gradient(145deg,rgba(18,30,49,.88),rgba(9,14,25,.7));
  border-radius:30px;box-shadow:var(--shadow);position:relative;overflow:hidden;display:grid;place-items:center;
  transition:transform .3s ease-out;will-change:transform;
}
.hero-card:after{content:"";position:absolute;inset:0;background:radial-gradient(circle at 30% 40%,rgba(97,218,251,.06),transparent 60%);pointer-events:none}
.orbit{width:260px;height:260px;border:1px solid rgba(97,218,251,.3);border-radius:50%;position:relative;animation:spin 16s linear infinite}
.orbit:before,.orbit:after{content:"";position:absolute;border:1px solid rgba(139,92,246,.3);border-radius:50%;inset:30px;transform:rotate(60deg)}
.orbit:after{inset:65px;transform:rotate(-45deg)}
.orbit2{position:absolute;width:200px;height:200px;border:1px dashed rgba(34,211,238,.2);border-radius:50%;animation:spin 24s linear infinite reverse}
.core{
  position:absolute;inset:75px;border-radius:50%;display:grid;place-items:center;
  background:radial-gradient(circle,#1e293b,#0b1220);border:1px solid rgba(97,218,251,.5);
  box-shadow:0 0 60px rgba(97,218,251,.18)
}
.core span{font-family:"Space Grotesk";font-weight:700;font-size:2.8rem;color:var(--accent)}
.core .engr-text{font-size:.55rem;letter-spacing:.3em;text-transform:uppercase;color:var(--engr-cyan);font-weight:600;margin-top:-4px}
.node{position:absolute;width:13px;height:13px;background:var(--accent);border-radius:50%;box-shadow:0 0 22px var(--accent)}
.n1{top:15px;left:50%}.n2{right:20px;bottom:55px;background:#a78bfa}.n3{left:20px;bottom:55px;background:#4ade80}
.n4{top:50%;left:10px;background:var(--engr-cyan);width:10px;height:10px}
@keyframes spin{to{transform:rotate(360deg)}}
.floating{
  position:absolute;padding:10px 14px;background:rgba(8,13,23,.9);border:1px solid var(--line);
  border-radius:10px;font-size:.72rem;color:#b9c8dc;animation:float 4s ease-in-out infinite;
  display:flex;align-items:center;gap:6px;backdrop-filter:blur(8px);z-index:2
}
.floating i{color:var(--accent);font-size:.75rem}
.f1{top:45px;right:25px}.f2{bottom:55px;left:22px;animation-delay:1s}.f3{top:46%;right:16px;animation-delay:2s}
@keyframes float{50%{transform:translateY(-10px)}}

section{padding:100px 0}
.section-head{margin-bottom:42px}
.eyebrow{color:var(--accent);font-size:.78rem;font-weight:700;letter-spacing:.18em;text-transform:uppercase;display:flex;align-items:center;gap:8px}
.eyebrow i{font-size:.75rem}
h2{font-family:"Space Grotesk";font-size:clamp(2rem,4vw,3.4rem);margin-top:8px;letter-spacing:-.04em}
.section-head p{color:var(--muted);max-width:650px;line-height:1.7;margin-top:12px}
.grid{display:grid;gap:18px}
.about-grid{grid-template-columns:1fr 1fr}
.card{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:25px;backdrop-filter:blur(12px);transition:.3s;position:relative}
.card:hover{transform:translateY(-5px);border-color:rgba(97,218,251,.28)}
.card h3{font-family:"Space Grotesk";margin-bottom:12px;display:flex;align-items:center;gap:9px}
.card h3 i{color:var(--accent);font-size:1rem}
.card p{color:var(--muted);line-height:1.75}

.skills{grid-template-columns:repeat(4,1fr)}
.skill{min-height:160px;transition:.35s}
.skill .icon{
  width:48px;height:48px;margin-bottom:15px;display:flex;align-items:center;justify-content:center;
  border-radius:13px;background:linear-gradient(145deg,rgba(97,218,251,.14),rgba(139,92,246,.14));
  border:1px solid rgba(148,163,184,.18);color:var(--accent);transition:.4s;font-size:1.2rem
}
.skill:hover{transform:translateY(-6px) scale(1.02);border-color:rgba(97,218,251,.35)}
.skill:hover .icon{transform:rotate(-8deg) scale(1.12);color:#fff;box-shadow:0 10px 26px rgba(97,218,251,.25)}
.skill small{color:var(--muted);display:block;margin-top:4px}

.langs{grid-template-columns:repeat(6,1fr);gap:14px}
.lang{min-height:130px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:9px;padding:18px 10px;transition:.35s}
.lang-badge{
  width:50px;height:50px;border-radius:12px;display:flex;align-items:center;justify-content:center;
  font-family:"Space Grotesk";font-weight:700;font-size:.9rem;letter-spacing:-.02em;
  box-shadow:0 10px 24px rgba(0,0,0,.35);transition:.4s
}
.lang:hover{transform:translateY(-6px);border-color:rgba(139,92,246,.4);box-shadow:0 14px 30px rgba(139,92,246,.15)}
.lang:hover .lang-badge{transform:translateY(-4px) rotate(-6deg) scale(1.08)}
.lang small{color:var(--muted);font-size:.72rem}
.php-badge{background:linear-gradient(135deg,#8993c4,#6a7bc2);color:#fff}
.py-badge{background:linear-gradient(135deg,#ffd43b 0 50%,#3776ab 50%);color:#0b1220}
.js-badge{background:#f7df1e;color:#1a1a1a}
.cs-badge{background:linear-gradient(135deg,#9b4f96,#68217a);color:#fff}
.c-badge{background:linear-gradient(135deg,#4f80c4,#2b5a94);color:#fff}
.cpp-badge{background:linear-gradient(135deg,#0081c2,#004a80);color:#fff}
@media(max-width:850px){.langs{grid-template-columns:repeat(3,1fr)}}
@media(max-width:520px){.langs{grid-template-columns:repeat(2,1fr)}}

.projects{grid-template-columns:repeat(2,1fr)}
.project{position:relative;overflow:hidden;min-height:280px}
.project:after{content:"";position:absolute;width:160px;height:160px;right:-50px;top:-50px;border-radius:50%;background:rgba(97,218,251,.08);filter:blur(4px)}
.tag{display:inline-block;padding:5px 10px;border-radius:999px;background:rgba(97,218,251,.09);color:var(--accent);font-size:.68rem;margin:4px 4px 0 0;font-weight:500}
.project p{margin:10px 0 18px}
.project .proj-icon{
  width:42px;height:42px;border-radius:10px;background:linear-gradient(135deg,rgba(37,99,235,.2),rgba(34,211,238,.15));
  display:flex;align-items:center;justify-content:center;color:var(--engr-cyan);font-size:1rem;margin-bottom:12px
}

.research{border-left:3px solid var(--accent);border-radius:0 18px 18px 0;position:relative}
.timeline{position:relative;display:grid;gap:18px}
.timeline:before{content:"";position:absolute;left:9px;top:10px;bottom:10px;width:1px;background:var(--line)}
.time-item{padding-left:35px;position:relative}
.time-item:before{content:"";position:absolute;left:4px;top:8px;width:11px;height:11px;border-radius:50%;background:var(--accent);box-shadow:0 0 15px var(--accent)}
.date{color:var(--accent);font-size:.76rem;font-weight:700;letter-spacing:.08em;display:flex;align-items:center;gap:6px}
.date i{font-size:.7rem}

.contact{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.contact .card{min-height:180px}
.contact .card h3 i{color:var(--accent)}
footer{padding:35px 0;border-top:1px solid var(--line);color:var(--muted);font-size:.85rem}
footer .footer-inner{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px}
footer i{color:var(--accent);margin-right:5px}

.ai{
  position:fixed;right:24px;bottom:24px;z-index:60;width:58px;height:58px;border:0;border-radius:50%;
  background:linear-gradient(135deg,var(--accent),#8b5cf6);cursor:pointer;
  box-shadow:0 12px 40px rgba(97,218,251,.25);font-size:1.3rem;color:#fff;
  display:flex;align-items:center;justify-content:center;transition:.3s
}
.ai:hover{transform:scale(1.08)}
.ai-panel{
  position:fixed;right:24px;bottom:94px;width:min(360px,calc(100vw - 32px));z-index:60;
  background:#0b1220;border:1px solid var(--line);border-radius:20px;box-shadow:var(--shadow);
  padding:18px;display:none
}
.ai-panel.show{display:block;animation:pop .25s ease}
@keyframes pop{from{opacity:0;transform:translateY(10px) scale(.98)}}
.ai-panel h3{font-family:"Space Grotesk";margin-bottom:6px;display:flex;align-items:center;gap:8px}
.ai-panel h3 i{color:var(--accent)}
.ai-panel p{font-size:.82rem;color:var(--muted);line-height:1.6}
.ai-answer{margin-top:12px;padding:12px;border-radius:12px;background:rgba(255,255,255,.04);font-size:.82rem;line-height:1.6;min-height:45px}
.ai-input{display:flex;gap:7px;margin-top:10px}
.ai-input input{min-width:0;flex:1;background:#111a2b;border:1px solid var(--line);color:white;padding:10px;border-radius:10px;outline:none}
.ai-input button{border:0;border-radius:10px;padding:0 14px;background:var(--accent);cursor:pointer;color:#061018;font-weight:600}
.reveal{opacity:0;transform:translateY(25px);transition:.7s}
.reveal.visible{opacity:1;transform:none}

@media(max-width:850px){
 .hero-grid,.about-grid,.contact,.projects{grid-template-columns:1fr}
 .skills{grid-template-columns:repeat(2,1fr)}
 .nav-links{display:none}.menu{display:block}
 .hero-card{min-height:360px}
 .orbit{width:200px;height:200px}
 .core{inset:55px}
 .core span{font-size:2rem}
 .orb{filter:blur(60px);opacity:.25}
}
@media(max-width:520px){
 .skills{grid-template-columns:1fr}
 section{padding:75px 0}
 .nav-inner{height:64px}
 .logo{font-size:1.2rem}
 .logo-icon{width:32px;height:32px;font-size:1rem}
 #particleCanvas{opacity:.35}
}

/* Accessibility: reduce motion */
@media (prefers-reduced-motion: reduce){
  *,*:before,*:after{animation-duration:.001ms !important;animation-iteration-count:1 !important;transition-duration:.001ms !important}
  #particleCanvas,.shooting-star{display:none}
}
</style>
</head>
<body>

<!-- ============ ANIMATED BACKGROUND ============ -->
<canvas id="particleCanvas"></canvas>
<div class="bg-orbs">
  <div class="orb orb1"></div>
  <div class="orb orb2"></div>
  <div class="orb orb3"></div>
  <div class="orb orb4"></div>
</div>
<div class="grid-overlay"></div>
<div class="circuit-overlay"></div>
<div class="stars" id="stars"></div>
<div class="shooting-star"></div>
<div class="shooting-star"></div>
<div class="shooting-star"></div>

<nav>
  <div class="container nav-inner">
    <a class="logo" href="#home">
      <div class="logo-icon"><i class="fas fa-microchip"></i></div>
      <div>JLS<span>.</span><div class="logo-sub">Engr &middot; Portfolio</div></div>
    </a>
    <div class="nav-links">
      <a href="#about"><i class="fas fa-user-astronaut"></i>About</a>
      <a href="#skills"><i class="fas fa-code"></i>Skills</a>
      <a href="#languages"><i class="fas fa-terminal"></i>Languages</a>
      <a href="#projects"><i class="fas fa-diagram-project"></i>Projects</a>
      <a href="#research"><i class="fas fa-flask"></i>Research</a>
      <a href="#experience"><i class="fas fa-briefcase"></i>Experience</a>
      <a href="#contact"><i class="fas fa-envelope"></i>Contact</a>
    </div>
    <button class="menu" onclick="document.querySelector('.nav-links').classList.toggle('mobile')"><i class="fas fa-bars"></i></button>
  </div>
</nav>

<main id="home">
<section class="hero">
  <div class="container hero-grid">
    <div class="reveal">
      <div class="engr-tag"><i class="fas fa-drafting-compass"></i> Engineer &middot; Builder &middot; Innovator</div>
      <div class="badge"><span class="dot"></span> Computer Engineering Graduate &middot; AI / ML / Systems</div>
      <h1>Building <span class="gradient">intelligent</span><br>technology.</h1>
      <p>
        I'm <strong>Joever L. Sayson</strong>, a Computer Engineering graduate and technology builder
        focused on Artificial Intelligence, Machine Learning, Computer Vision, hardware,
        system configuration, and practical automation.
      </p>
      <div class="buttons">
        <a class="btn primary" href="#projects"><i class="fas fa-rocket"></i>Explore My Work</a>
        <a class="btn" href="#research"><i class="fas fa-book-open"></i>View Research</a>
      </div>
    </div>
    <div class="hero-card reveal" id="heroCard">
      <div class="orbit2"></div>
      <div class="orbit">
        <div class="core">
          <span>AI</span>
          <div class="engr-text">Engr</div>
        </div>
        <i class="node n1"></i><i class="node n2"></i><i class="node n3"></i><i class="node n4"></i>
      </div>
      <div class="floating f1"><i class="fas fa-eye"></i> YOLOv3 &middot; CNN</div>
      <div class="floating f2"><i class="fas fa-brain"></i> Transformers &middot; Keras</div>
      <div class="floating f3"><i class="fas fa-microchip"></i> Hardware + Systems</div>
    </div>
  </div>
</section>

<section id="about">
<div class="container">
  <div class="section-head reveal">
    <div class="eyebrow"><i class="fas fa-user-astronaut"></i> 01 &middot; About</div>
    <h2>Engineer with a builder mindset.</h2>
    <p>Combining software intelligence with hardware and system-level problem solving.</p>
  </div>
  <div class="grid about-grid">
    <div class="card reveal">
      <h3><i class="fas fa-id-badge"></i>Who I am</h3>
      <p>
        Computer Engineering graduate with hands-on experience developing AI and Computer Vision projects,
        configuring computer systems, troubleshooting hardware/software, and integrating intelligent
        technologies with real-world applications.
      </p>
    </div>
    <div class="card reveal">
      <h3><i class="fas fa-tools"></i>What I work with</h3>
      <p>
        My technical interests include machine learning, image classification, object detection,
        computer vision, embedded systems, system configuration, networking fundamentals, and
        software-hardware integration.
      </p>
    </div>
  </div>
</div>
</section>

<section id="skills">
<div class="container">
  <div class="section-head reveal">
    <div class="eyebrow"><i class="fas fa-code"></i> 02 &middot; Expertise</div>
    <h2>Technical toolkit.</h2>
  </div>
  <div class="grid skills">
    <div class="card skill reveal">
      <div class="icon"><i class="fas fa-brain"></i></div>
      <h3>AI & Machine Learning</h3>
      <small>CNN &middot; Transformers &middot; Keras &middot; Model development</small>
    </div>
    <div class="card skill reveal">
      <div class="icon"><i class="fas fa-eye"></i></div>
      <h3>Computer Vision</h3>
      <small>YOLOv3 &middot; CNN &middot; Image Classification &middot; Object Detection</small>
    </div>
    <div class="card skill reveal">
      <div class="icon"><i class="fas fa-microchip"></i></div>
      <h3>Hardware</h3>
      <small>PC assembly &middot; Troubleshooting &middot; Embedded systems &middot; Sensors</small>
    </div>
    <div class="card skill reveal">
      <div class="icon"><i class="fas fa-desktop"></i></div>
      <h3>System Configuration</h3>
      <small>Windows &middot; Software setup &middot; Networking &middot; System deployment</small>
    </div>
    <div class="card skill reveal">
      <div class="icon"><i class="fas fa-project-diagram"></i></div>
      <h3>Circuit Design & PCB</h3>
      <small>EAGLE CAD &middot; Schematic design &middot; PCB layout &middot; PCB board fabrication</small>
    </div>
    <div class="card skill reveal">
      <div class="icon"><i class="fas fa-database"></i></div>
      <h3>Databases</h3>
      <small>MySQL &middot; PostgreSQL &middot; Database design &middot; Query optimization</small>
    </div>
  </div>
</div>
</section>

<section id="languages">
<div class="container">
  <div class="section-head reveal">
    <div class="eyebrow"><i class="fas fa-terminal"></i> 02b &middot; Languages</div>
    <h2>Programming languages.</h2>
  </div>
  <div class="grid langs">
    <div class="card lang reveal"><div class="lang-badge php-badge">php</div><h3 style="font-size:.95rem">PHP</h3><small>Backend / Web</small></div>
    <div class="card lang reveal"><div class="lang-badge py-badge">Py</div><h3 style="font-size:.95rem">Python</h3><small>AI / ML / CV</small></div>
    <div class="card lang reveal"><div class="lang-badge js-badge">JS</div><h3 style="font-size:.95rem">JavaScript</h3><small>Web / Frontend</small></div>
    <div class="card lang reveal"><div class="lang-badge cs-badge">C#</div><h3 style="font-size:.95rem">C#</h3><small>Applications</small></div>
    <div class="card lang reveal"><div class="lang-badge c-badge">C</div><h3 style="font-size:.95rem">C</h3><small>Embedded / Systems</small></div>
    <div class="card lang reveal"><div class="lang-badge cpp-badge">C++</div><h3 style="font-size:.95rem">C++</h3><small>Systems / Embedded</small></div>
  </div>
</div>
</section>

<section id="projects">
<div class="container">
  <div class="section-head reveal">
    <div class="eyebrow"><i class="fas fa-diagram-project"></i> 03 &middot; Selected Work</div>
    <h2>Projects that solve problems.</h2>
  </div>
  <div class="grid projects">
    <article class="card project reveal">
      <div class="proj-icon"><i class="fas fa-seedling"></i></div>
      <h3>Pest & Disease Monitoring System (Thesis)</h3>
      <p>Thesis project: AI-powered agricultural monitoring for Lakatan banana farming that combines a CNN-based image classification model with a built-in AI chatbot for farmer support, fully integrated across hardware (camera/sensor capture) and software (detection, classification, and chat interface) in one system.</p>
      <span class="tag">CNN</span><span class="tag">AI Chatbot</span><span class="tag">Computer Vision</span><span class="tag">Smart Agriculture</span><span class="tag">Hardware + Software</span>
    </article>
    <article class="card project reveal">
      <div class="proj-icon"><i class="fas fa-coins"></i></div>
      <h3>Fund Control System (IoT + Stock Management)</h3>
      <p>A hardware-and-software fund/stock control project: an Arduino Uno paired with a waterproof sensor handles the hardware side, while a web-based stock management system deployed on Vercel handles inventory and fund tracking &mdash; designed as an integrated embedded + web solution.</p>
      <span class="tag">Arduino Uno</span><span class="tag">Waterproof Sensor</span><span class="tag">Stock Management</span><span class="tag">Vercel</span>
    </article>
    <article class="card project reveal">
      <div class="proj-icon"><i class="fas fa-camera"></i></div>
      <h3>Computer Vision Detection Projects</h3>
      <p>Hands-on experimentation with different computer vision approaches for object detection and image understanding using YOLOv3, CNN-based models, and Transformer architectures.</p>
      <span class="tag">YOLOv3</span><span class="tag">CNN</span><span class="tag">Transformers</span><span class="tag">Keras</span>
    </article>
    <article class="card project reveal">
      <div class="proj-icon"><i class="fas fa-tools"></i></div>
      <h3>Hardware & System Configuration</h3>
      <p>Practical work involving computer hardware, operating system configuration, software installation, troubleshooting, device setup, and hardware-software integration.</p>
      <span class="tag">Hardware</span><span class="tag">Windows</span><span class="tag">Troubleshooting</span>
    </article>
    <article class="card project reveal">
      <div class="proj-icon"><i class="fas fa-robot"></i></div>
      <h3>Robotics & Embedded Systems</h3>
      <p>Experience integrating microcontrollers, sensors, motors, communication, and intelligent processing into competition and automation projects.</p>
      <span class="tag">Arduino</span><span class="tag">Raspberry Pi</span><span class="tag">Sensors</span><span class="tag">Robotics</span>
    </article>
  </div>
</div>
</section>

<section id="research">
<div class="container">
  <div class="section-head reveal">
    <div class="eyebrow"><i class="fas fa-flask"></i> 04 &middot; Research</div>
    <h2>Published research.</h2>
  </div>
  <div class="card research reveal">
    <div class="date"><i class="fas fa-book"></i> PUBLISHED RESEARCH</div>
    <h3 style="font-size:1.45rem;margin-top:9px">Pest and Disease Monitoring System for Banana Lakatan Farming Using CNN Algorithm</h3>
    <p style="margin-top:13px">
      Research focused on applying Convolutional Neural Networks to agricultural image analysis,
      with the goal of improving pest and disease monitoring for Lakatan banana farming.
    </p>
    <div style="margin-top:17px"><span class="tag">Agricultural AI</span><span class="tag">CNN</span><span class="tag">Image Classification</span><span class="tag">Smart Agriculture</span></div>
  </div>
  <div class="card reveal" style="margin-top:18px">
    <h3><i class="fas fa-trophy"></i>Competitive Technology</h3>
    <p>Participated in regional robotics and technology competitions, including a Sumobot competition where the team achieved 1st Place in 2026.</p>
  </div>
</div>
</section>

<section id="experience">
<div class="container">
  <div class="section-head reveal">
    <div class="eyebrow"><i class="fas fa-briefcase"></i> 05 &middot; Experience</div>
    <h2>From classroom to real systems.</h2>
  </div>
  <div class="timeline">
    <div class="card time-item reveal">
      <div class="date"><i class="fas fa-hospital"></i> CURRENT WORK</div>
      <h3>Medical Records Archiver &mdash; Mindanao Medical Center, Inc.</h3>
      <p>Currently handling medical records archiving, organization, and management at Mindanao Medical Center, Inc.</p>
    </div>
    <div class="card time-item reveal">
      <div class="date"><i class="fas fa-brain"></i> AI / MACHINE LEARNING</div>
      <h3>AI & Computer Vision Development</h3>
      <p>Developed and experimented with CNN, YOLOv3, Transformer-based approaches, and Keras for image analysis and computer vision applications.</p>
    </div>
    <div class="card time-item reveal">
      <div class="date"><i class="fas fa-microchip"></i> HARDWARE & SYSTEMS</div>
      <h3>Hardware & System Configuration</h3>
      <p>Hands-on experience in hardware troubleshooting, computer setup, operating system configuration, software installation, and system support.</p>
    </div>
    <div class="card time-item reveal">
      <div class="date"><i class="fas fa-flask"></i> RESEARCH & ENGINEERING</div>
      <h3>Research & Technology Projects</h3>
      <p>Applied engineering concepts to agricultural AI, embedded systems, automation, robotics, and practical technology solutions.</p>
    </div>
  </div>
</div>
</section>

<section id="contact">
<div class="container">
  <div class="section-head reveal">
    <div class="eyebrow"><i class="fas fa-envelope"></i> 06 &middot; Contact</div>
    <h2>Let's build something useful.</h2>
  </div>
  <div class="grid contact">
    <div class="card reveal">
      <h3><i class="fas fa-user-tie"></i>Joever L. Sayson</h3>
      <p>Computer Engineering Graduate<br>AI &middot; Machine Learning &middot; Computer Vision<br>Hardware &middot; System Configuration<br><br>
      <i class="fas fa-envelope" style="color:var(--accent)"></i> <a href="mailto:saysonjoever9@gmail.com" style="color:var(--accent)">saysonjoever9@gmail.com</a></p>
    </div>
    <div class="card reveal">
      <h3><i class="fas fa-handshake"></i>Open to opportunities</h3>
      <p>Interested in roles and projects involving IT support, software, AI/ML, computer vision, hardware, systems, and technology research.</p>
    </div>
  </div>
</div>
</section>
</main>

<footer>
  <div class="container footer-inner">
    <div>&copy; 2026 Joever L. Sayson &middot; Computer Engineering Portfolio</div>
    <div><i class="fas fa-microchip"></i> <i class="fas fa-drafting-compass"></i> <i class="fas fa-robot"></i></div>
  </div>
</footer>

<button class="ai" onclick="toggleAI()" aria-label="Open AI assistant"><i class="fas fa-robot"></i></button>
<div class="ai-panel" id="aiPanel">
  <h3><i class="fas fa-robot"></i> Joever AI Assistant</h3>
  <p>Ask about Joever's skills, projects, research, or experience.</p>
  <div class="ai-answer" id="aiAnswer">Hi! Ask me something about this portfolio.</div>
  <div class="ai-input">
    <input id="aiInput" placeholder="Ask a question..." onkeydown="if(event.key==='Enter')askAI()">
    <button onclick="askAI()"><i class="fas fa-paper-plane"></i></button>
  </div>
</div>

<script>
/* ============ BACKGROUND: STAR FIELD ============ */
(function(){
  const stars = document.getElementById('stars');
  const count = 60;
  let html = '';
  for(let i=0;i<count;i++){
    const x = Math.random()*100;
    const y = Math.random()*100;
    const delay = (Math.random()*3).toFixed(2);
    const size = (Math.random()*1.5+0.5).toFixed(1);
    html += '<div class="star" style="left:'+x+'%;top:'+y+'%;animation-delay:'+delay+'s;width:'+size+'px;height:'+size+'px"></div>';
  }
  stars.innerHTML = html;
})();

/* ============ BACKGROUND: PARTICLE NETWORK CANVAS ============ */
(function(){
  const canvas = document.getElementById('particleCanvas');
  const ctx = canvas.getContext('2d');
  let W, H, particles = [];
  const PARTICLE_COUNT = 55;
  const MAX_DIST = 140;
  const COLORS = ['#61dafb','#8b5cf6','#22d3ee','#4ade80'];

  function resize(){
    W = canvas.width = window.innerWidth;
    H = canvas.height = window.innerHeight;
  }

  function initParticles(){
    particles = [];
    for(let i=0;i<PARTICLE_COUNT;i++){
      particles.push({
        x: Math.random()*W,
        y: Math.random()*H,
        vx: (Math.random()-0.5)*0.35,
        vy: (Math.random()-0.5)*0.35,
        r: Math.random()*1.6+0.6,
        c: COLORS[Math.floor(Math.random()*COLORS.length)]
      });
    }
  }

  function draw(){
    ctx.clearRect(0,0,W,H);

    // Draw connections
    for(let i=0;i<particles.length;i++){
      for(let j=i+1;j<particles.length;j++){
        const a = particles[i], b = particles[j];
        const dx = a.x - b.x, dy = a.y - b.y;
        const dist = Math.sqrt(dx*dx + dy*dy);
        if(dist < MAX_DIST){
          const alpha = (1 - dist/MAX_DIST) * 0.35;
          ctx.strokeStyle = 'rgba(97,218,251,' + alpha + ')';
          ctx.lineWidth = 0.5;
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.stroke();
        }
      }
    }

    // Draw particles
    for(const p of particles){
      p.x += p.vx;
      p.y += p.vy;

      // Wrap around edges
      if(p.x < 0) p.x = W;
      if(p.x > W) p.x = 0;
      if(p.y < 0) p.y = H;
      if(p.y > H) p.y = 0;

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI*2);
      ctx.fillStyle = p.c;
      ctx.shadowColor = p.c;
      ctx.shadowBlur = 8;
      ctx.fill();
      ctx.shadowBlur = 0;
    }

    requestAnimationFrame(draw);
  }

  // Respect reduced motion preference
  if(!window.matchMedia('(prefers-reduced-motion: reduce)').matches){
    resize();
    initParticles();
    draw();
    window.addEventListener('resize', ()=>{ resize(); initParticles(); });
  } else {
    canvas.style.display = 'none';
  }
})();

/* ============ HERO CARD PARALLAX ============ */
(function(){
  const heroCard = document.getElementById('heroCard');
  if(!heroCard) return;
  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const heroSection = document.querySelector('.hero');
  heroSection.addEventListener('mousemove', function(e){
    const rect = heroSection.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width - 0.5;
    const y = (e.clientY - rect.top) / rect.height - 0.5;
    heroCard.style.transform = 'perspective(1000px) rotateY(' + (x*8) + 'deg) rotateX(' + (-y*8) + 'deg) translateZ(10px)';
  });
  heroSection.addEventListener('mouseleave', function(){
    heroCard.style.transform = '';
  });
})();

/* ============ SCROLL REVEAL ============ */
const observer = new IntersectionObserver(entries=>{
  entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible')})
},{threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));

/* ============ AI CHATBOT ============ */
function toggleAI(){document.getElementById('aiPanel').classList.toggle('show')}

function askAI(){
  const q=document.getElementById('aiInput').value.toLowerCase().trim();
  const a=document.getElementById('aiAnswer');
  if(!q)return;
  let answer="I can answer questions about Joever's portfolio, skills, projects, research, languages, and experience.";
  if(q.includes('skill')||q.includes('technology')){
    answer="Joever's focus includes AI/ML, Computer Vision, CNN, YOLOv3, Transformers, Keras, hardware troubleshooting, system configuration, circuit design/PCB layout with EAGLE, MySQL & PostgreSQL databases, and embedded systems.";
  }else if(q.includes('language')||q.includes('php')||q.includes('python')||q.includes('javascript')||q.includes('c#')||q.includes('c++')){
    answer="He programs in PHP, Python, JavaScript, C#, C, and C++.";
  }else if(q.includes('database')||q.includes('sql')||q.includes('mysql')||q.includes('postgres')){
    answer="He has experience working with MySQL and PostgreSQL databases.";
  }else if(q.includes('pcb')||q.includes('circuit')||q.includes('eagle')){
    answer="He builds circuits and designs PCB layouts and PCB boards using EAGLE CAD.";
  }else if(q.includes('fund')||q.includes('stock')||q.includes('vercel')||q.includes('arduino')){
    answer="One of his recent builds is a Fund Control System combining an Arduino Uno with a waterproof sensor for the hardware side, and a web-based stock management system deployed on Vercel for the software side.";
  }else if(q.includes('work')||q.includes('job')||q.includes('medical')){
    answer="He currently works as a Medical Records Archiver at Mindanao Medical Center, Inc.";
  }else if(q.includes('contact')||q.includes('email')||q.includes('gmail')){
    answer="You can reach Joever at saysonjoever9@gmail.com.";
  }else if(q.includes('project')){
    answer="Key projects include his thesis - a Pest and Disease Monitoring System for Banana Lakatan Farming using CNN with a built-in AI chatbot, combining hardware and software - plus a Fund Control System using Arduino Uno + a waterproof sensor with a Vercel-hosted stock management web app.";
  }else if(q.includes('research')||q.includes('paper')){
    answer="Joever is a published research author of a study on a CNN-based Pest and Disease Monitoring System for Banana Lakatan farming, which also features a built-in AI chatbot and combines hardware and software.";
  }else if(q.includes('education')||q.includes('graduate')){
    answer="Joever is a Computer Engineering graduate from Holy Trinity College in General Santos City.";
  }else if(q.includes('computer vision')||q.includes('yolo')||q.includes('cnn')||q.includes('transformer')){
    answer="His Computer Vision experience includes YOLOv3, CNN-based models, Transformer architectures, image classification, object detection, and Keras.";
  }else if(q.includes('hardware')||q.includes('system')){
    answer="He has hands-on experience with hardware troubleshooting, system configuration, software setup, embedded systems, sensors, circuit/PCB design, and hardware-software integration.";
  }
  a.textContent=answer;
  document.getElementById('aiInput').value='';
}

document.querySelector('.menu').addEventListener('click',function(){
  var nl=document.querySelector('.nav-links');
  nl.style.display = (nl.style.display==='flex') ? '' : 'flex';
  if(window.innerWidth<=850){
    nl.style.position='absolute';
    nl.style.top='64px';
    nl.style.right='4%';
    nl.style.padding='18px';
    nl.style.background='#0b1220';
    nl.style.border='1px solid rgba(148,163,184,.15)';
    nl.style.borderRadius='14px';
    nl.style.flexDirection='column';
    nl.style.zIndex='100';
  }
});
</script>
</body>
</html>
'''

path = Path(__file__).resolve().parent / "index.html"
path.write_text(html, encoding="utf-8")
print("Generated:", path)