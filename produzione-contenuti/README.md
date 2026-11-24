# Produzione contenuti

Macro cartella delle skill per creare contenuti (reel, video ads, grafiche animate, montaggi, idee di format).
Sull'account Claude il punto d'ingresso unico è la skill **`social`** (`/social`): legge la richiesta e lancia la skill giusta.

## Skill dell'agenzia (installate sull'account)

| Skill | Fase | Quando |
|---|---|---|
| `social` | ingresso | smista la richiesta verso le skill qui sotto |
| `reel-fuori-scala` | ricerca | cosa sta funzionando nella nicchia, swipe file, idee di format |
| `audit-contenuti-instagram` | analisi | cosa ha funzionato o floppato, report organico |
| `punteggio-profilo-instagram` | analisi | audit del profilo, prospect, onboarding |
| `repurpose-contenuti` | idee | da un contenuto lungo a una settimana di post |
| `ricciardi-copy` | scrittura | tutti i testi: script, caption, promo, format |
| `marketing-psychology` | scrittura (supporto) | leve psicologiche |
| `montaggio-video-drive` | montaggio | girati dal Drive: tagli, 9:16, audio, sottotitoli, copertine (motore di taglio consigliato: `esterne/video-use`) |
| `motion-grafiche` | grafica animata | **nuova**, in questa cartella: aperture, prezzi, grafici, traguardi, loghi animati |
| `video-making` | video da zero | skill generica di Anthropic per video nuovi senza girato |

## Skill esterne messe da parte (originali, licenza MIT)

`esterne/` contiene gli originali da cui è stata adattata `motion-grafiche` e le skill esterne di editing. Non vanno caricati sull'account così come sono: sono in inglese, pensati per SaaS e newsletter, e farebbero partire skill doppie.

| Origine | Skill tenute | Perché |
|---|---|---|
| charlie947/motion-graphics-skills | `reel-export`, `motion-effects` (16 ricette), `animated-chart`, `milestone-reveal`, `reference-to-motion`, `motion-brief-writer`, `brand-intake` | metodo per animazioni in codice rese in MP4, export reel che Meta accetta, scomposizione dei riferimenti |
| Moh4696/open-3d-skills | `frame-capture`, `alpha-cutout` | registrare una pagina animata in MP4 fluido; scontornare un video (piatto o persona) su sfondo trasparente |
| browser-use/video-use | `video-use` (completa, con gli script) | **editing**: monta i girati partendo dalla trascrizione (tagli sulle parole, scelta dei ciak, grade, sottotitoli, audio). Verificata e resa gratuita con la trascrizione locale `transcribe_whisper.py`: vedi `esterne/video-use/ADATTAMENTO-AGENZIA.md` |

Scartate dal pacchetto charlie947: launch-video, apple-launch-film, vox-explainer, newsletter-promo, loop-cover, model-showdown, title-sequence-3d, motion-prompt-writer (sono per lanci SaaS e newsletter, oppure scrivono prompt per "Claude Motion", che sull'account non è disponibile).

## Le skill del post r/claudeskills ("9 lesser-known Claude skills for visual work"): classificazione

| Skill | Categoria | Dove | Verdetto |
|---|---|---|---|
| motion-graphics-skills (charlie947) | motion | produzione-contenuti | **adottata**, adattata in `motion-grafiche` |
| open-3d-skills (Moh4696) | motion / 3D | produzione-contenuti | parziale: tenute `frame-capture` e `alpha-cutout`, il resto è siti 3D |
| tastemaker (codeswithroh) | riferimenti visivi | siti-e-landing | per le landing e i siti clienti, non per i contenuti |
| dembrandt-skills (dembrandt) | riferimenti visivi | siti-e-landing | tenute `extract-design` (colori e font dal sito del locale) e `algorithmic-color-palette`; le altre 28 sono UX per app |
| brand-identity-skill (fatihaydost) | design | siti-e-landing | logo, font e palette per un locale senza identità; utile anche per Food Media Production |
| styleseed (bitjaru) | design | scartata | doppione di tastemaker, pensata per app |
| genjutsu (AThevon) | motion web | scartata per ora | animazioni di siti e app (anche iOS e Android), file enormi; da riprendere solo per i siti clienti |
| claude-drawing-skill (cloveric) | arte | scartata | in cinese, file da 740 KB che pesa su ogni chiamata, illustrazioni non utili al food |
| genart-skill (camilleroux) | arte | scartata | arte generativa astratta |
| forever-ai-components (isas1) | componenti | scartata | catalogo di componenti web, non è una skill |
