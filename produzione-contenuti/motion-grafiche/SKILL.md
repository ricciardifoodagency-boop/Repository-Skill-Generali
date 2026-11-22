---
name: motion-grafiche
description: "Crea motion graphic in codice (HTML animato reso in MP4 o GIF) per l'agenzia e i clienti food: apertura reel col nome dell'offerta, prezzo che si svela, grafici animati per i report, traguardi, testimonianze, chiusura col logo. Usala anche per rifare un reel o un'ad di riferimento."
---

# Motion grafiche (uso interno Ricciardi Food Agency)

Rispondi sempre in italiano. Non fare domande di conferma durante il lavoro: procedi e riferisci alla fine.
Questa skill non monta i girati: per tagli, sottotitoli e audio sui video del Drive c'è `montaggio-video-drive`.
Qui si crea grafica animata da zero, in codice, da usare da sola o da inserire in un montaggio.

Adattata dal pacchetto MIT "Motion Graphics Skill Pack" di Charlie Hills (charlie947/motion-graphics-skills). Gli originali sono in `produzione-contenuti/esterne/` nel repository Repository-Skill-Generali.

## 1. Cosa serve prima di partire
- **Testi**: le parole sullo schermo restano identiche a come le dà l'utente. Se vanno scritte da zero, passano da `ricciardi-copy`.
- **Numeri**: solo numeri veri, dati dall'utente o presi dai report. Mai inventati. I numeri d'esempio portano la scritta "esempio" su ogni fotogramma.
- **Brand**: per l'agenzia usa il rosso #c32a2d. Per un cliente usa logo, colori e font del locale. Se non li fornisce l'utente, cercali sul sito o sul profilo Instagram del locale. Mai la grafica di un altro cliente.
- **Formato**: per i reel e le ads 1080x1920 (9:16), per il feed 1080x1350 (4:5) o 1080x1080 (1:1).
- **Loop o fermo**: il loop si ripete all'infinito (post, GIF). Il fermo esegue il movimento una volta e resta sull'ultimo fotogramma (sotto la voce, o come pezzo del montaggio).

Se manca qualcosa di essenziale (un testo, un numero), dillo in una riga e usa un segnaposto visibile tipo `[PREZZO]`, senza fermarti.

## 2. Scegli l'effetto in base al lavoro

| Lavoro | Effetto |
|---|---|
| Apertura reel o ad col nome dell'offerta o della degustazione | scritta rivelata da una maschera, oppure scritta elastica |
| Prezzo o offerta che si svela | immagine rivelata (foto del piatto), poi il prezzo entra come scritta mascherata |
| Report organico mensile al cliente (follower, interazioni, visualizzazioni) | grafico animato: barre che diventano linea, numero che sale, prima e dopo |
| Traguardo (follower del locale, "oltre 100 imprenditori") | traguardo: punti che si raccolgono nel numero vero, linea sotto, etichetta |
| Tre testimonianze, tre piatti o tre offerte in fila | pila a molla: le card entrano una alla volta |
| Le fasi del servizio dell'agenzia | cambio di prospettiva a livelli |
| Chiusura di un reel o di un'ad | logo che si compone da particelle |

Le ricette complete dei 16 effetti (stato iniziale e finale, tempi, il dettaglio che lo rende curato) sono in `esterne/charlie947-motion-graphics/motion-effects/references/effects.md`. Il grafico animato e il traguardo hanno le loro schede: `animated-chart` e `milestone-reveal`.

## 3. Rifare un riferimento
Quando l'utente manda un reel o un'ad che gli piace (link, screenshot o fotogrammi):
1. Scomponilo in cinque righe: ritmo (quanto dura ogni inquadratura), passaggio tra le scene, come arrivano le scritte, colore e luce, l'unica idea che regge tutto il video.
2. Da lì prendi solo ritmo, passaggi e idea. Non prendere logo, testi, colori o personaggi.
3. Il tema e le parole sono del cliente. I ganci si reinventano per il locale, non si ricopiano.
4. Scrivi il piano scena per scena: tempi in secondi, che sommati danno la durata esatta, e un'idea visiva per scena. Poi costruiscilo.

## 4. Costruisci il file
Un solo file `effetto.html`, con queste regole:
1. **Un solo orologio**: ogni fotogramma si calcola dal tempo. Serve `window.seek(secondi)`, che disegna il fotogramma esatto di quel momento, in qualsiasi ordine. Niente `setTimeout`, niente animazioni CSS che vanno da sole, niente casualità senza seme.
2. **Loop di 8 secondi**: movimento da 0 a 2,2 s, pausa fino a 6,6 s, ritorno entro 8 s; `seek(0)` e `seek(8)` sono identici. In modalità fermo, dopo 6,6 s resta sull'ultimo fotogramma. Nei reel e nelle ads il movimento va accorciato a circa 1,5 s: 8 secondi sono troppi per uno spezzone.
3. **Nella pausa qualcosa resta vivo** (una barra, un luccichio), altrimenti il loop sembra fermo.
4. **Autonomo**: font incorporati e caricati prima di `seek(0)`, immagini inline, nessuna richiesta di rete.
5. **Zona sicura dei reel**: scritte e loghi tra y 360 e y 1420, fuori dagli ultimi 120 px a destra.
6. **Stile**: un oggetto che si trasforma in un altro, non una dissolvenza tra due immagini. Gli elementi partono sfalsati di un battito, non tutti insieme. Movimento ease-out, senza rimbalzi.
7. **Regole dell'agenzia**: titoli non tutti in maiuscolo; prima il beneficio e poi la caratteristica; mai "pesce fresco" (si dice qualità e accurata selezione).

## 5. Controlla prima di mostrare
Cattura i fotogrammi a 0; 1; 2,2; 4,4; 6,6; 7,9 e 8 secondi e guardali tutti:
- 0 e 8 sono identici (solo per il loop);
- 0, 1 e 2,2 sono diversi tra loro;
- nessun testo è tagliato o esce dal suo riquadro;
- fermo sul 4,4, il messaggio si capisce da quel fotogramma da solo;
- colori e font sono quelli del brand.
Correggi, ricattura e solo dopo vai avanti.

## 6. Esporta
`python3 scripts/render.py /percorso/assoluto/effetto.html out.mp4 <secondi> [larghezza] [altezza] [fps]` (di default 1080x1920 a 30 fps)
Lo script usa Chrome e Playwright già presenti nell'ambiente: chiama `window.seek()` per ogni fotogramma e codifica in H.264. L'output è yuv420p, range tv, bt709, con traccia audio muta e faststart, cioè un file che Instagram e Meta accettano senza sbiadire i colori. Se la skill è installata sull'account senza lo script, ricrealo: pagina caricata con `?render`, uno screenshot PNG per fotogramma inviato a ffmpeg da stdin, con le stesse impostazioni di codifica.
- GIF: `ffmpeg -i out.mp4 -vf "fps=20,scale=720:-1:flags=lanczos,split[a][b];[a]palettegen[p];[b][p]paletteuse" -loop 0 out.gif`
- Video orizzontale da portare in verticale con titolo sopra: segui `esterne/charlie947-motion-graphics/reel-export`.
- Controllo finale: `ffprobe -v error -show_entries stream=codec_name,width,height,pix_fmt,color_range -of compact out.mp4` deve dare h264, 1080x1920, yuv420p, tv.

## 7. Consegna
Invia all'utente l'MP4 (e la GIF se serve) con due fotogrammi di controllo (2,2 e 4,4). Se va in un'inserzione, si può caricare in bozza su Meta con `meta-ads-setup`. Se va dentro un montaggio, passa il file a `montaggio-video-drive`.
