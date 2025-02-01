from core.speech_to_text import ecouter_et_transcrire

texte_transcrit = ecouter_et_transcrire()
if texte_transcrit:
    print(f"Texte transcrit : {texte_transcrit}")
