# video-use: note per Ricciardi Food Agency

Origine: https://github.com/browser-use/video-use (licenza MIT, gratuita e open source).
Copiata qui il 24/11/2026 senza le immagini del README (cartella `static/` e `poster.html`).

## Cosa fa
Monta un video partendo dalla trascrizione parola per parola: taglia su silenzi e confini delle parole, sceglie la ripresa migliore tra più ciak, mette la correzione colore, le animazioni sovrapposte e i sottotitoli (sempre per ultimi), normalizza l'audio e si ricontrolla da solo i punti di taglio prima di consegnare.

## Verifica fatta (24/11/2026, ambiente cloud di Claude)
- Gli script girano con ffmpeg, Pillow, numpy e librosa.
- Prova completa riuscita: trascrizione → `takes_packed.md` → due tagli → grade `warm_cinematic` → sottotitoli → normalizzazione audio → `final.mp4`.
- Il codice non manda dati da nessuna parte, tranne `transcribe.py`, che carica l'audio su ElevenLabs.

## Gratis davvero: la trascrizione
La skill originale trascrive con **ElevenLabs Scribe**, che richiede una chiave API (piano gratuito limitato, poi a pagamento).
Per non pagare abbiamo aggiunto `helpers/transcribe_whisper.py`: trascrive in locale con faster-whisper e scrive lo stesso formato, così il resto della skill funziona uguale.

    pip install faster-whisper
    python helpers/transcribe_whisper.py video.mp4 --language it --model small --prompt "nomi di piatti e del locale"

Differenze rispetto a Scribe: non distingue chi parla (tutto S0), non segna risate e applausi, i tempi delle parole sono un po' meno precisi. Per questo il margine dei tagli va tenuto alto, sui 100-200 ms.
Il modello si scarica da Hugging Face, che dall'ambiente cloud è raggiungibile. Se servono due parlanti separati (es. un'intervista al titolare), conviene Scribe con la chiave.

## Regole dell'agenzia che cambiano il metodo originale
- **Niente attesa di conferma**: l'originale chiede l'ok sul piano prima di tagliare (regola 11). Per noi il piano si scrive in 4-8 righe e poi si procede, riferendo alla fine.
- **Sottotitoli**: massimo 3 parole per schermata, parola attiva in rosso #c32a2d (o nel colore del locale), font Inter ExtraBold, maiuscolo/minuscolo naturale, dentro la zona sicura del reel.
- **Formato**: 1080x1920, H.264, audio a -14 LUFS per i social.
- **Copy**: le parole dette e scritte non si cambiano; caption e testi passano da `ricciardi-copy`.
- **Girati dal Drive**: scarico, copertine e consegna seguono `montaggio-video-drive`; video-use è il motore di taglio.
- **Animazioni sovrapposte**: si possono fare con `motion-grafiche` e passare a video-use come `overlays` nell'EDL.
- **Sotto-agenti**: l'originale fa le animazioni in parallelo con il tool Agent. In chat su claude.ai si fanno una alla volta.

## Come usarla
- **In Claude Code**: copiare questa cartella in `.claude/skills/video-use/` del progetto, poi `pip install -e .` e `pip install faster-whisper`.
- **Sull'account Claude**: per ora non è caricata, perché servono gli script in `helpers/` che il caricamento della sola SKILL.md non porta con sé. In chat si possono prendere da qui (repository nel contesto della sessione).
