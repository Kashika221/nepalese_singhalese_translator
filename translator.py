from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

model_name = "facebook/mbart-large-50-many-to-many-mmt"
tok = MBart50TokenizerFast.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)

def translate(text, src_lang_code, tgt_lang_code="en_XX"):
    # src_lang_code example: "ne_NP" or "si_LK" (depending on model's tokens)
    tok.src_lang = src_lang_code
    input_ids = tok(text, return_tensors="pt", truncation=True).input_ids
    out = model.generate(input_ids, forced_bos_token_id=tok.lang_code_to_id[tgt_lang_code])
    return tok.batch_decode(out, skip_special_tokens=True)[0]

nepali_text = "नेपाल एक सुन्दर देश हो।"
sinhala_text = "ශ්‍රී ලංකාව සුන්දර දිවයිනක් වේ."

print("Nepali → English:", translate(nepali_text, src_lang_code="ne_NP"))
print("Sinhala → English:", translate(sinhala_text, src_lang_code="si_LK"))