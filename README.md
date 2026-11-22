# Repository Skill Generali

Store centrale delle skill di Ricciardi Food Agency, divise in macro cartelle.
Le skill nascono e si aggiornano qui; poi si caricano sull'account Claude dell'agenzia.

## Come usarle in Claude Code

In una sessione di Claude Code su un altro progetto, aggiungi questo repo:

> aggiungi il repo `ricciardifoodagency-boop/Repository-Skill-Generali`

Claude Code carica in automatico solo le skill in `.claude/skills/` (formati file e design generali).
Le macro cartelle sono il catalogo: per usare una skill in Claude Code, copiane la cartella in `.claude/skills/` del progetto.

## Macro cartelle

| Cartella | Contenuto | Punto d'ingresso sull'account |
|---|---|---|
| `produzione-contenuti/` | reel, video ads, montaggio, grafiche animate, idee di format | `/social` |
| `siti-e-landing/` | landing, siti clienti, identità visiva | `landing-food-grafica`, `lancio-funnel` |
| `.claude/skills/` | formati file (docx, xlsx, pptx, pdf) e design generali, da anthropics/skills | caricate in automatico |

## Classificazione di tutte le skill dell'account

| Macro area | Skill | Come si chiamano |
|---|---|---|
| **Produzione contenuti** | social (ingresso), reel-fuori-scala, audit-contenuti-instagram, punteggio-profilo-instagram, repurpose-contenuti, ricciardi-copy, marketing-psychology, montaggio-video-drive, motion-grafiche, video-making | `/social` oppure la richiesta diretta |
| **Advertising Meta** | meta-ads-setup, ad-library-monitoring, competitor-analysis (+ ricciardi-copy per i testi) | richiesta diretta |
| **Funnel, landing e siti** | landing-food-grafica, lancio-funnel | richiesta diretta |
| **Metodo di lavoro** | grill-me, handoff | solo su richiesta esplicita (`/grill-me`, `/handoff`) |
| **Ricerca e tecnica** | deep-research, reverse-engineering, skill-creator | richiesta diretta |
| **Formati file** (Anthropic) | docs, docx, xlsx, pptx, pdf, google-workspace | automatiche in base al formato |
| **Browser e computer** (Anthropic) | chrome-browser, built-in-browser, computer-use | automatiche quando si usa il browser o il PC |
| **Poco usate** (Anthropic) | morning, import-memory | si possono disattivare dalle impostazioni skill |

Le skill dell'agenzia derivano dai playbook del Secondo Cervello (`04-tech-ai/agenti-e-skill.md`): quando cambia un playbook si aggiorna la skill, non il contrario.
