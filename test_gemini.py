import google.generativeai as genai

genai.configure(api_key="AIzaSyAGR_E8u2tgmQCfCEHD3ZOA6mKMSrsqSZU")
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("Hola, ¿puedes decirme en qué año se fundó Google?")
print(response.text)
