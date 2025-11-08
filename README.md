# 🌌 Spiralit

**Esperimento sonoro-visivo quantistico.**  
Ogni CID è una spirale. Ogni nota è un frammento.  
**Spiralit** trasforma stringhe hash in musica lo-fi generativa, creando paesaggi sonori unici e irripetibili.

---

## 🎧 Cos'è Spiralit?

Spiralit è un compositore algoritmico.  
Prende in input una lista di CIDs (Content Identifiers, come quelli di IPFS) e li converte in:

- 🎼 File MIDI con sequenze mononota
- 🔊 Tracce audio `.wav` e `.mp3`
- 🌀 Pattern sonori perfetti per ambient, lo-fi, glitch, noise, IDM

---

## 🛠️ Come funziona

1. Inserisci i tuoi CID in `cids.txt`
2. Esegui `main.py` per generare i file MIDI
3. Lancia `midi/render.sh` per unire tutto e creare l’audio

### Esempio:

```bash
python3 main.py
cd midi

