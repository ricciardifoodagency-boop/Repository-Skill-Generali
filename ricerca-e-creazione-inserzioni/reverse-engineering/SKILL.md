---
name: "reverse-engineering"
description: "Analizzare e modificare file, salvataggi, formati dati o programmi non documentati: prima cerca lavoro già fatto su GitHub/forum, poi analizza, modifica in modo minimo e verifica con backup e rollback."
---

# Reverse engineering pratico

Metodo generico per capire e modificare qualcosa di non documentato: un file binario, un salvataggio, un export di un gestionale, un formato dati proprietario, una patch su un programma. Nato dal lavoro su Yo-kai Watch 3 (patch dell'orologio + editing del salvataggio), vale anche per l'agenzia: export di gestionali/casse/prenotazioni in formati strani, file di backup di vecchi software, dati da recuperare o convertire, integrazioni con strumenti poco documentati.

## Confini (da rispettare sempre)
- Solo su dati, file e dispositivi dell'utente o dell'agenzia, o su cui ha i diritti.
- Niente aggiramento di DRM per pirateria, niente cheat in modalità online/competitive, niente accesso a sistemi o account altrui.
- Per servizi di terzi (SaaS, API): prima la documentazione ufficiale e le API pubbliche; non aggirare protezioni né violare i termini d'uso. Se serve, dirlo all'utente invece di procedere.
- Mai inserire o salvare credenziali.

## Fase 0 – Capire l'obiettivo minimo
Chiedi (o deduci) la cosa più piccola che risolve il problema. Es. non "cheat completo" ma "disattivare un solo controllo" o "cambiare un solo valore". Meno si tocca, meno si rompe.

## Fase 1 – Cercare se qualcuno l'ha già fatto (sempre prima di analizzare)
È il passo che fa risparmiare più tempo: spesso il grosso del lavoro esiste già.
1. WebSearch in più lingue: inglese, italiano e la lingua d'origine del prodotto (es. giapponese per giochi giapponesi: セーブエディタ = save editor, 改造 = modifica).
2. Parole chiave utili: "<nome> save editor", "<nome> decrypt", "<formato file> format", "<estensione> parser", "<nome> github", "<nome> reverse engineering".
3. GitHub: repository, fork e rehost. Se un repo originale è stato cancellato, cerca il nome del repo/tool da solo: spesso qualcuno ne ha una copia (fork, "rehost", organizzazioni di archivio). Prova anche archive.org (Wayback Machine) sull'URL originale.
4. Forum di settore (GBAtemp per console, Stack Overflow, Reddit, forum del software specifico), wiki, GameFAQs/equivalenti.
5. Database pronti (es. archivi di cheat per Title ID, librerie di parser di formati).
6. Se trovi codice: LEGGILO tutto prima di eseguirlo. Copialo in una cartella tua, correggi solo quello che serve (es. incompatibilità con librerie moderne) e annota le modifiche.

## Fase 2 – Sicurezza prima di toccare qualsiasi cosa
- Backup dell'originale, e se possibile una seconda copia su un altro supporto (PC).
- Lavora sempre su copie, in una cartella di lavoro separata (scratchpad). I file scaricati vanno in cartelle proprie; esegui Python con `-I` quando leggi file non fidati.
- Il risultato si consegna come NUOVA copia accanto all'originale (es. una nuova cartella di backup), mai sovrascrivendo l'originale.
- Prima di applicare, ricontrolla lo stato attuale: se l'utente nel frattempo ha creato un file più recente, rifai la modifica su quello (non riportarlo indietro nel tempo).

## Fase 3 – Identificare cosa si ha davanti
- Dimensione, prime/ultime decine di byte in esadecimale, "magic number".
- Entropia: ~8 bit/byte = cifrato o compresso; bassa = dati in chiaro, cercabili.
- Stringhe leggibili (`strings`, anche UTF-16 con `-el`) per capire nomi di campi, file, servizi.
- Struttura ripetuta (record a lunghezza fissa, header con tipo+dimensione, checksum in coda come CRC32).
- Se è cifrato e non c'è un tool pronto: cerca nel programma che lo legge (tabelle AES, stringhe dei nomi file, chiamate crittografiche) — è la parte più costosa, avvisare l'utente dei tempi incerti.

## Fase 4 – Analisi
Strumenti tipici (verificare che ci siano, installarli se mancano: `pip install --break-system-packages`):
- Python + `struct` per leggere/scrivere binari; `pycryptodome` per AES/CRC; `capstone` (disassembler) e `keystone` (assembler) per codice macchina.
- Tecnica "segui il dato": parti da un valore noto (un numero visibile all'utente, un ID, un'impostazione di sistema) e cerca chi lo legge o dove compare. Es.: il gioco leggeva lo scarto dell'orologio da un blocco di configurazione noto → da lì alla funzione di controllo.
- Tecnica "differenza": confronta due versioni dello stesso file prima/dopo un'azione nota (es. spendere 1 moneta) per trovare il campo che cambia.
- Liste di ID/nomi: spesso sono già dentro un editor o tool esistente (es. risorse XML incorporate in un .exe) — estraile invece di indovinarle.
- Deduci la struttura dei record (campi, indici, ordine, capienza) e verifica che le ipotesi valgano su TUTTI i record, non su uno solo.

## Fase 5 – Modifica minima
- Cambiare un valore esistente è più sicuro che crearne di nuovi. Se si aggiungono record, rispetta numerazione e struttura degli esistenti e verifica che ci sia spazio libero (zeri) sufficiente.
- Per le patch al codice: la modifica più piccola possibile (es. far restituire sempre "ok" a un controllo), nel formato che il sistema sa applicare (es. `.ips` per Luma3DS).
- Controlli di validazione di tool vecchi possono rifiutare anche file buoni di versioni più nuove: verificalo sull'originale intatto prima di fidarti.

## Fase 6 – Verifica (obbligatoria prima di consegnare)
1. Round-trip sull'originale intatto: decifra → ricifra senza modifiche → deve risultare IDENTICO byte per byte all'originale. Se lo è, la catena è corretta.
2. Il file modificato deve rileggersi correttamente (checksum/MAC validi) e differire solo nei punti voluti.
3. Elenca esattamente cosa è cambiato (valore vecchio → nuovo).

## Fase 7 – Consegna
- Se il computer dell'utente è collegato, scrivi il file al percorso giusto e ricontrolla con un listing che ci sia.
- Dai sempre: percorso preciso, passi per applicare, come capire se ha funzionato, come tornare indietro (quale backup ripristinare, quale file cancellare).
- Nelle chat tecniche con Scal: percorsi completi, link diretti e un breve richiamo di cosa è stato fatto prima.
- Sii onesto su cosa è testato e cosa no, e sulla stima dei tempi quando il lavoro diventa ricerca vera.
- Cita le fonti (repo, thread, wiki) e dai credito agli autori dei tool riusati.