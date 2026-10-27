<!DOCTYPE html>
<html lang="ckb" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#0B0906">
<title>کوردپایرەت · KurdPirate</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Pirata+One&family=Vazirmatn:wght@400;500;600;700;800&family=Cinzel:wght@500;700&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.js"></script>
<style>
:root{
  --bg:#0B0906;
  --bg-2:#120D08;
  --panel:#1B140C;
  --panel-2:#241A0F;
  --hair:#3A2C17;
  --hair-2:#2A2013;
  --parchment:#EFE2C3;
  --ink:#F4ECD8;
  --muted:#A6926C;
  --muted-dim:#7A6B4E;
  --gold:#D4A72C;
  --gold-bright:#F0C860;
  --gold-deep:#8A6A16;
  --blood:#8A2A24;
  --blood-bright:#C4453B;
  --emerald:#3E7D5A;
  --r:16px;
  --r-lg:22px;
  --r-pill:999px;
  --display:"Pirata One",serif;
  --serif:"Cinzel",serif;
  --sans:"Vazirmatn",system-ui,sans-serif;
  --ease:cubic-bezier(.22,1,.36,1);
  --spring:cubic-bezier(.34,1.56,.64,1);
}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{margin:0;padding:0;background:var(--bg);color:var(--ink);font-family:var(--sans);overflow-x:hidden}
body{
  min-height:100vh;
  background:
    radial-gradient(120% 60% at 50% -10%, rgba(212,167,44,.10), transparent 60%),
    radial-gradient(90% 50% at 100% 110%, rgba(138,42,36,.10), transparent 60%),
    var(--bg);
}
/* subtle grain */
body::before{
  content:"";position:fixed;inset:0;pointer-events:none;z-index:1;opacity:.05;mix-blend-mode:overlay;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='120' height='120'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>");
}
button{font-family:inherit;border:none;background:none;color:inherit;cursor:pointer}
input,textarea{font-family:inherit;color:inherit}
img{display:block;max-width:100%}
a{color:inherit;text-decoration:none}
::selection{background:var(--gold);color:#20160a}

#app{position:relative;z-index:2;max-width:520px;margin:0 auto;min-height:100vh;padding-bottom:92px}

/* ===== Top bar ===== */
.topbar{
  position:sticky;top:0;z-index:30;display:flex;align-items:center;justify-content:space-between;
  padding:calc(env(safe-area-inset-top) + 14px) 16px 12px;
  background:linear-gradient(180deg, rgba(11,9,6,.96), rgba(11,9,6,.82) 70%, transparent);
  backdrop-filter:blur(10px);
}
.icon-btn{width:42px;height:42px;border-radius:var(--r-pill);display:grid;place-items:center;background:var(--panel);border:1px solid var(--hair);color:var(--parchment);font-size:1.15rem;transition:transform .3s var(--spring),background .3s}
.icon-btn:active{transform:scale(.88)}
.brand{display:flex;align-items:center;gap:10px}
.brand img{width:34px;height:34px;border-radius:9px;box-shadow:0 4px 14px -6px rgba(212,167,44,.5)}
.brand .word{font-family:var(--display);font-size:1.5rem;letter-spacing:.5px;color:var(--gold-bright);
  text-shadow:0 2px 0 #00000080;}

/* ===== Drawer ===== */
.scrim{position:fixed;inset:0;background:rgba(6,4,2,.6);backdrop-filter:blur(2px);z-index:40;opacity:0;pointer-events:none;transition:opacity .35s var(--ease)}
.scrim.open{opacity:1;pointer-events:auto}
.drawer{
  position:fixed;top:0;bottom:0;right:0;width:min(78vw,340px);z-index:41;background:var(--bg-2);
  border-left:1px solid var(--hair);transform:translateX(100%);transition:transform .4s var(--ease);
  padding:calc(env(safe-area-inset-top) + 20px) 22px 20px;overflow-y:auto;
}
.drawer.open{transform:translateX(0)}
.drawer-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:28px}
.drawer-title{font-family:var(--display);font-size:1.4rem;color:var(--gold-bright)}
.drawer-link{display:flex;align-items:center;justify-content:space-between;padding:15px 4px;border-bottom:1px solid var(--hair-2);font-size:1.02rem;color:var(--parchment);font-weight:600}
.drawer-link .chev{color:var(--muted-dim);font-size:.85rem}

/* ===== Views ===== */
.view{display:none;padding:0 16px 8px;animation:fadeIn .4s var(--ease)}
.view.active{display:block}
@keyframes fadeIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}

/* ===== Section headers ===== */
.sec-title{font-family:var(--display);font-size:1.5rem;color:var(--gold-bright);margin:22px 2px 14px;display:flex;align-items:center;gap:10px}
.sec-title .rule{flex:1;height:1px;background:linear-gradient(90deg,var(--hair),transparent)}

/* ===== Hero ===== */
.hero{position:relative;border-radius:var(--r-lg);overflow:hidden;height:220px;margin-top:6px;box-shadow:0 20px 40px -22px rgba(0,0,0,.7);border:1px solid var(--hair)}
.hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg, transparent 30%, rgba(9,7,4,.94) 96%)}
.hero-body{position:absolute;left:0;right:0;bottom:0;padding:16px;z-index:2}
.hero-badge{display:inline-flex;align-items:center;gap:4px;background:rgba(11,9,6,.7);border:1px solid var(--hair);border-radius:var(--r-pill);padding:3px 10px;font-size:.78rem;font-weight:700;color:var(--gold-bright);margin-bottom:8px}
.hero-title{font-family:var(--display);font-size:1.7rem;color:var(--parchment);line-height:1.15;margin-bottom:6px;text-shadow:0 2px 6px #000}
.hero-meta{font-size:.82rem;color:var(--muted);margin-bottom:12px}
.hero-actions{display:flex;gap:10px}
.hero-dots{position:absolute;top:12px;left:14px;display:flex;gap:5px;z-index:2}
.hero-dots span{width:6px;height:6px;border-radius:50%;background:rgba(239,226,195,.35)}
.hero-dots span.on{background:var(--gold-bright);width:16px;border-radius:4px}

/* ===== Buttons ===== */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:12px 20px;border-radius:var(--r-pill);font-weight:700;font-size:.92rem;transition:transform .25s var(--spring),filter .25s}
.btn:active{transform:scale(.95)}
.btn-gold{background:linear-gradient(180deg,var(--gold-bright),var(--gold));color:#221805;box-shadow:0 10px 24px -10px rgba(212,167,44,.55)}
.btn-ghost{background:rgba(239,226,195,.08);color:var(--parchment);border:1px solid var(--hair)}
.btn-blood{background:linear-gradient(180deg,var(--blood-bright),var(--blood));color:#fff0ee}
.btn-block{width:100%}
.btn-sm{padding:9px 16px;font-size:.8rem}

/* ===== Category chips ===== */
.chip-row{display:flex;gap:8px;overflow-x:auto;padding:2px 2px 6px;scrollbar-width:none}
.chip-row::-webkit-scrollbar{display:none}
.chip{flex:0 0 auto;padding:8px 16px;border-radius:var(--r-pill);background:var(--panel);border:1px solid var(--hair);font-size:.82rem;font-weight:600;color:var(--muted);white-space:nowrap;transition:.25s}
.chip.on{background:var(--gold);color:#221805;border-color:var(--gold)}

/* ===== Movie grid & cards ===== */
.grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.grid.cw{grid-template-columns:none;grid-auto-flow:column;grid-auto-columns:64%;overflow-x:auto;padding-bottom:6px;scrollbar-width:none}
.grid.cw::-webkit-scrollbar{display:none}
.card{position:relative;border-radius:var(--r);overflow:hidden;background:var(--panel);border:1px solid var(--hair);cursor:pointer;transition:transform .3s var(--spring)}
.card:active{transform:scale(.96)}
.card .poster-wrap{position:relative;aspect-ratio:2/3;overflow:hidden;background:var(--panel-2)}
.card .poster-wrap img{width:100%;height:100%;object-fit:cover}
.badge{position:absolute;top:8px;display:flex;align-items:center;gap:3px;background:rgba(11,9,6,.78);backdrop-filter:blur(4px);border-radius:var(--r-pill);padding:3px 8px;font-size:.72rem;font-weight:800}
.badge.rating{right:8px;color:var(--gold-bright)}
.badge.adult{left:8px;background:var(--blood);color:#fff}
.badge.progress{left:0;right:0;bottom:0;top:auto;border-radius:0;padding:0;height:4px;background:rgba(255,255,255,.15)}
.badge.progress i{display:block;height:100%;background:var(--gold-bright)}
.card .fav{position:absolute;bottom:8px;left:8px;width:30px;height:30px;border-radius:50%;background:rgba(11,9,6,.65);display:grid;place-items:center;font-size:.95rem;color:var(--parchment)}
.card .fav.on{color:var(--blood-bright)}
.card .info{padding:9px 10px 12px}
.card .t{font-size:.86rem;font-weight:700;color:var(--parchment);line-height:1.25;
  display:-webkit-box;-webkit-line-clamp:1;-webkit-box-orient:vertical;overflow:hidden}
.card .m{font-size:.72rem;color:var(--muted-dim);margin-top:3px}

/* ===== Categories page tiles ===== */
.cat-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:8px}
.cat-tile{display:flex;align-items:center;justify-content:space-between;padding:20px 16px;border-radius:var(--r);
  background:linear-gradient(160deg, var(--panel-2), var(--panel));border:1px solid var(--hair);font-weight:700;font-size:.98rem}
.cat-tile .ic{width:38px;height:38px;border-radius:11px;background:rgba(212,167,44,.14);color:var(--gold-bright);display:grid;place-items:center;font-size:1.05rem}

/* ===== Search ===== */
.search-box{position:relative;margin-top:8px}
.search-box input{width:100%;padding:14px 46px 14px 16px;border-radius:var(--r-pill);background:var(--panel);border:1px solid var(--hair);color:var(--parchment);font-size:.95rem}
.search-box input:focus{outline:none;border-color:var(--gold-deep)}
.search-box .sic{position:absolute;left:16px;top:50%;transform:translateY(-50%);color:var(--muted)}
.empty{text-align:center;padding:60px 20px;color:var(--muted)}
.empty .ic{font-size:2.4rem;margin-bottom:10px;opacity:.6}

/* ===== Bottom nav ===== */
.navbar{
  position:fixed;bottom:0;left:0;right:0;z-index:30;max-width:520px;margin:0 auto;
  display:flex;justify-content:space-around;align-items:center;
  padding:10px 6px calc(env(safe-area-inset-bottom) + 8px);
  background:rgba(18,13,8,.92);backdrop-filter:blur(14px);border-top:1px solid var(--hair);
}
.nav-btn{display:flex;flex-direction:column;align-items:center;gap:3px;color:var(--muted-dim);font-size:.68rem;font-weight:700;padding:4px 10px;border-radius:14px;transition:.3s}
.nav-btn .ic{font-size:1.25rem}
.nav-btn.active{color:var(--gold-bright)}

/* ===== Auth / account view ===== */
.auth-wrap{padding-top:26px;text-align:center}
.auth-wrap .logo{width:96px;height:96px;margin:0 auto 14px;border-radius:22px;box-shadow:0 16px 34px -14px rgba(212,167,44,.5)}
.auth-wrap h1{font-family:var(--display);font-size:1.7rem;color:var(--gold-bright);margin:0 0 4px}
.auth-wrap p.tag{color:var(--muted);font-size:.85rem;margin:0 0 26px;font-family:var(--serif);letter-spacing:.5px}
.field{position:relative;margin-bottom:12px;text-align:right}
.field input{width:100%;padding:14px 16px;border-radius:14px;background:var(--panel);border:1px solid var(--hair);color:var(--parchment);font-size:.95rem}
.field input:focus{outline:none;border-color:var(--gold-deep)}
.auth-switch{margin-top:18px;font-size:.85rem;color:var(--muted)}
.auth-switch b{color:var(--gold-bright);cursor:pointer}
.auth-err{color:var(--blood-bright);font-size:.82rem;margin-top:8px;min-height:1em}

.profile-card{display:flex;align-items:center;gap:14px;padding:18px;border-radius:var(--r-lg);background:var(--panel);border:1px solid var(--hair);margin-top:10px}
.avatar{width:56px;height:56px;border-radius:50%;background:linear-gradient(160deg,var(--gold-bright),var(--gold-deep));display:grid;place-items:center;font-family:var(--display);font-size:1.5rem;color:#20160a}
.profile-name{font-weight:800;font-size:1.05rem;color:var(--parchment)}
.profile-sub{font-size:.78rem;color:var(--muted-dim);margin-top:2px}
.list-row{display:flex;align-items:center;justify-content:space-between;padding:15px 4px;border-bottom:1px solid var(--hair-2);font-weight:600;color:var(--parchment)}
.list-row .ic{margin-inline-end:12px;color:var(--gold-bright)}
.footer-credit{text-align:center;color:var(--muted-dim);font-size:.72rem;margin:36px 0 10px;font-family:var(--serif);letter-spacing:.5px}

/* ===== Detail overlay ===== */
.detail{position:fixed;inset:0;z-index:50;background:var(--bg);transform:translateY(100%);transition:transform .4s var(--ease);overflow-y:auto}
.detail.open{transform:translateY(0)}
.detail-hero{position:relative;height:320px}
.detail-hero img{width:100%;height:100%;object-fit:cover}
.detail-hero::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg, rgba(11,9,6,.2), var(--bg) 92%)}
.detail-close{position:absolute;top:calc(env(safe-area-inset-top) + 14px);right:16px;z-index:2;width:40px;height:40px;border-radius:50%;background:rgba(11,9,6,.6);backdrop-filter:blur(6px);display:grid;place-items:center;color:var(--parchment)}
.detail-body{padding:0 18px 40px;margin-top:-46px;position:relative;z-index:2}
.detail-title{font-family:var(--display);font-size:1.9rem;color:var(--parchment);text-shadow:0 2px 8px #000}
.detail-meta{display:flex;align-items:center;gap:10px;margin:8px 0 16px;font-size:.85rem;color:var(--muted)}
.detail-meta .r{color:var(--gold-bright);font-weight:800}
.detail-actions{display:flex;gap:10px;margin-bottom:20px}
.detail-actions .fav-lg{width:48px;height:48px;flex:0 0 48px;border-radius:50%;background:var(--panel);border:1px solid var(--hair);display:grid;place-items:center;font-size:1.15rem;color:var(--parchment)}
.detail-actions .fav-lg.on{color:var(--blood-bright);border-color:var(--blood)}
.detail-desc{color:var(--muted);font-size:.92rem;line-height:1.7;margin-bottom:20px}
.player-wrap{border-radius:var(--r);overflow:hidden;background:#000;margin-bottom:22px;border:1px solid var(--hair)}
.player-wrap video{width:100%;display:block;max-height:56vw}
.rate-row{display:flex;align-items:center;gap:6px;margin-bottom:22px;flex-wrap:wrap}
.rate-star{font-size:1.3rem;color:var(--hair);cursor:pointer;transition:.15s}
.rate-star.on{color:var(--gold-bright)}
.comment-box{display:flex;gap:8px;margin-bottom:18px}
.comment-box textarea{flex:1;resize:none;height:44px;padding:12px 14px;border-radius:14px;background:var(--panel);border:1px solid var(--hair);color:var(--parchment);font-size:.88rem}
.comment{padding:12px 0;border-bottom:1px solid var(--hair-2)}
.comment .who{font-weight:700;font-size:.85rem;color:var(--gold-bright)}
.comment .txt{font-size:.86rem;color:var(--parchment);margin-top:3px;line-height:1.5}
.comment .when{font-size:.7rem;color:var(--muted-dim);margin-top:4px}

/* ===== Toast ===== */
.toast{position:fixed;bottom:110px;left:50%;transform:translateX(-50%) translateY(20px);z-index:60;
  background:var(--panel-2);border:1px solid var(--hair);color:var(--parchment);padding:11px 20px;border-radius:var(--r-pill);
  font-size:.85rem;font-weight:600;opacity:0;pointer-events:none;transition:.35s var(--ease);box-shadow:0 14px 30px -14px rgba(0,0,0,.6)}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}

/* ===== Skeleton loading ===== */
.skel{background:linear-gradient(100deg, var(--panel) 30%, var(--panel-2) 50%, var(--panel) 70%);background-size:200% 100%;animation:shimmer 1.4s infinite}
@keyframes shimmer{to{background-position:-200% 0}}
.spinner{width:34px;height:34px;border-radius:50%;border:3px solid var(--hair);border-top-color:var(--gold-bright);animation:spin 1s linear infinite;margin:40px auto}
@keyframes spin{to{transform:rotate(360deg)}}
</style>
</head>
<body>
<div id="app">

  <!-- ===== Top bar ===== -->
  <div class="topbar">
    <button class="icon-btn" id="btn-menu" aria-label="menu">☰</button>
    <div class="brand"><img src="data:image/webp;base64,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" alt="KurdPirate"><span class="word">KURDPIRATE</span></div>
    <button class="icon-btn" id="btn-topsearch" aria-label="search">⌕</button>
  </div>

  <!-- ===== Drawer ===== -->
  <div class="scrim" id="scrim"></div>
  <div class="drawer" id="drawer">
    <div class="drawer-head">
      <span class="drawer-title">پۆلەکان</span>
      <button class="icon-btn" id="btn-drawer-close">✕</button>
    </div>
    <button class="drawer-link" data-cat="type:series">زنجیرەکان <span class="chev">›</span></button>
    <button class="drawer-link" data-cat="type:movie">فیلمەکان <span class="chev">›</span></button>
    <button class="drawer-link" data-cat="type:short">کورتەفیلم <span class="chev">›</span></button>
    <button class="drawer-link" data-cat="type:anime">ئەنیمەیی <span class="chev">›</span></button>
    <button class="drawer-link" data-cat="lang:kurdish">کوردی <span class="chev">›</span></button>
    <button class="drawer-link" data-cat="lang:farsi">فارسی <span class="chev">›</span></button>
    <button class="drawer-link" data-cat="coming:1">بەرنامەوانە <span class="chev">›</span></button>
    <button class="drawer-link" data-cat="top:1">Top 250 ⭐ <span class="chev">›</span></button>
  </div>

  <!-- ===== HOME ===== -->
  <div class="view active" id="view-home">
    <div class="hero" id="hero"><div class="spinner"></div></div>

    <div id="cw-section" style="display:none">
      <div class="sec-title">بەردەوامبوونەوە<span class="rule"></span></div>
      <div class="grid cw" id="grid-cw"></div>
    </div>

    <div class="sec-title">نوێترین فیلمەکان<span class="rule"></span></div>
    <div class="grid" id="grid-movies"><div class="spinner"></div></div>

    <div class="sec-title">نوێترین زنجیرەکان<span class="rule"></span></div>
    <div class="grid" id="grid-series"></div>
  </div>

  <!-- ===== CATEGORIES ===== -->
  <div class="view" id="view-categories">
    <div class="sec-title">پۆلەکان<span class="rule"></span></div>
    <div class="cat-grid">
      <button class="cat-tile" data-cat="type:series"><span>زنجیرەکان</span><span class="ic">▤</span></button>
      <button class="cat-tile" data-cat="type:movie"><span>فیلمەکان</span><span class="ic">▥</span></button>
      <button class="cat-tile" data-cat="type:short"><span>کورتەفیلم</span><span class="ic">▶</span></button>
      <button class="cat-tile" data-cat="type:anime"><span>ئەنیمەیی</span><span class="ic">★</span></button>
      <button class="cat-tile" data-cat="lang:kurdish"><span>کوردی</span><span class="ic">⌂</span></button>
      <button class="cat-tile" data-cat="lang:farsi"><span>فارسی</span><span class="ic">ⓘ</span></button>
      <button class="cat-tile" data-cat="coming:1"><span>بەرنامەوانە</span><span class="ic">▦</span></button>
      <button class="cat-tile" data-cat="top:1"><span>Top 250</span><span class="ic">⭐</span></button>
    </div>
  </div>

  <!-- ===== FILTERED LIST (categories / search results) ===== -->
  <div class="view" id="view-list">
    <div class="sec-title"><span id="list-title">ئەنجامەکان</span><span class="rule"></span></div>
    <div class="grid" id="grid-list"></div>
    <div class="empty" id="list-empty" style="display:none"><div class="ic">🏴☠️</div>هیچ نەدۆزرایەوە</div>
  </div>

  <!-- ===== SEARCH ===== -->
  <div class="view" id="view-search">
    <div class="search-box">
      <span class="sic">⌕</span>
      <input id="search-input" placeholder="گەڕان بۆ فیلم یان زنجیرە...">
    </div>
    <div class="grid" id="grid-search" style="margin-top:18px"></div>
    <div class="empty" id="search-empty"><div class="ic">🔍</div>ناوی فیلم، زنجیرە، یان ئەکتەرێک بنووسە بۆ گەڕان.</div>
  </div>

  <!-- ===== WATCHLIST ===== -->
  <div class="view" id="view-watchlist">
    <div class="sec-title">لیستەکەم<span class="rule"></span></div>
    <div class="grid" id="grid-watchlist"></div>
    <div class="empty" id="watchlist-empty" style="display:none"><div class="ic">🦴</div>هێشتا هیچت زیاد نەکردووە بۆ لیستەکەت</div>
  </div>

  <!-- ===== ACCOUNT (login/profile) ===== -->
  <div class="view" id="view-account"></div>

  <!-- ===== Bottom nav ===== -->
  <div class="navbar">
    <button class="nav-btn" data-nav="account"><span class="ic">☺</span>پرۆفایل</button>
    <button class="nav-btn" data-nav="watchlist"><span class="ic">▤</span>لیستەکەم</button>
    <button class="nav-btn" data-nav="categories"><span class="ic">▦</span>پۆلەکان</button>
    <button class="nav-btn" data-nav="search"><span class="ic">⌕</span>گەڕان</button>
    <button class="nav-btn active" data-nav="home"><span class="ic">⌂</span>سەرەکی</button>
  </div>
</div>

<!-- ===== Movie detail overlay ===== -->
<div class="detail" id="detail"></div>
<div class="toast" id="toast"></div>

<script>
/* ============================================================
   کوردپایرەت · KurdPirate — RODO_Dev
   Single-file frontend wired to Supabase (auth + movies data)
   ============================================================ */
const SUPABASE_URL = "https://ukihakfkmixdaimfceql.supabase.co";
const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVraWhha2ZrbWl4ZGFpbWZjZXFsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODUyNjY5NTIsImV4cCI6MjEwMDg0Mjk1Mn0.BydaaHCI6xXzCD5brKEs6DZ1R8TFKIjop9xmlDZ7MvM";
const sb = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

const LOGO320 = "data:image/webp;base64,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... (25 KB left)