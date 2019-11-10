import speech_recognition as sr
import json

SPEECH_JSON=json.dumps({'type': 'service_account','project_id': 'curious-clone-258512','private_key_id': '223d719570d38d5813294e3339aaca1811db6d30','private_key': '-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCu4SZ9kseKsh0a\ngTaIn4zMwenoCNmbEul6HFQiXa5li/vPSolELE31+cqVg3oIBstPoRoyOhzE+y2N\nSbaos/0SoXNLR/he7BmvVn26ecOAruGLPffEQDlNBR+mljvUZcTU8ILdcdAMuQ1H\nNvxokDwV/jiFsJq/LQr+1PIhPq9wZLcz7d6xTTfixn89pZY+VwDrim14PRUBf4ke\nRZ0PkL3amFvHpYt1ByVkvt9wxxAtlqzmDiT9ixnsTpnzm5mbFkmPMOYbkHmFSjfN\naBYVzUxEN2cGDndOwnh0bk2c/2hMI0GEVUfYyc0Su1drW/9OsVo6S5ElTDpMh5GD\no+UpsJ5dAgMBAAECggEAAJR6uiEtR4ex1yiXjMgFir0qMIFR3blxQu8z1RbGTvCf\n14g695n8ljTCYSxsGYu3FHpQqdr7V5Z59fw20M0i4Be6jvKSzTwT8N9uEAjDxyfW\neF/3vS8+xfpDca5alt+IZBZn1UbmJD7yTRzzEqTZiHO2LiLCBlgmitP3QnjS9yH0\n+NpqyIVW4VHXPTPoZP4JU1N458owRI93cuCgG6a+IYdDWTPtJzdXccKiA21jA6Xf\n+ScQuUaf1LGkEZXIX6O/BDob86MNaEWTV18O3hgbAYTxTaNpLFiJd8IJuqnfnNVp\n4sNcIX7VU5gIXSNR53oDv5P+AMWbOT3Bb1j+pcEQBwKBgQDlQR1J8qLk3hexIOIm\nSZJ+8JqY62RlRJe1AvUQlz6Xz40N7hC+qPnHyrLUH85lOBP5tZSNzcycjlTO/YV8\nfINOvhE0xLSpJXxhSDdyvV2QjJpe8jeeRMxTLtgfcBYtp51dTLl6vkmWG+ha57wm\n2ynlpr5UoZzblmenHiggCn8aKwKBgQDDSBURfqsHnvcAXovh+366bGkfMvjBXSUQ\nBVqpQI1LVDEN3nk1HZPy5GiuyhB16vT4emCqjfpDR+IuIkKU7KEugLfWUWKzz0sO\nBdr3oVKXZTqkoKs9RNsGDLWow6F6wZmnxhVn/AE5PLtP75iPlYcwvpgT0nfEWUW7\n1iEAjywNlwKBgQDFVK38R9D0xUKJYa+nmy5w+3Nm6z8Id+lJkpkUxcrH64wTkHZz\nVolh8tTJB/OlZoazKxwKjzlvDIhtfwVWaOqxbaLr0+FZsv2D0yB/MAaIdK4vybgc\nEEX719eJ//XnKF6ov3Dr+Tzn62+uR8fJfl5q4YL04ANfc/AWhjutkLtk7wKBgDbO\nTyNm0mdEJPxUjJuysqFtdZ9M9eWG17UEW6putHj0uwOycYAHuhMMKZkMmswNUg0+\ng0y6pgcl8IOUF+2l76KWe4HJu5LNVbosyISBISXeQjQb55M9dN7gyEcCCJrkJNSi\nUjWp00oWElff3YhGpfd3NkUx520SxPBvqzl19R4nAoGAJYMPnH28S1XfE8eBFuSb\nu3ujBJ7HJmvh0XKMOKQAHezRDXkUwqKfbacfRLwOwQyYhfXqqUwDm3xj7T2NcyI9\nAWeH8Msrap3f6+AVwzwdEw0TN680BMM8xfH67hj4VSTbSzMj+ztytV1NNSN6Yjk3\n5X96o+2uQb6EGjiFMUXmWWI=\n-----END PRIVATE KEY-----\n','client_email': 'angels-of-angela@curious-clone-258512.iam.gserviceaccount.com','client_id': '114472607784801307277','auth_uri': 'https://accounts.google.com/o/oauth2/auth','token_uri': 'https://oauth2.googleapis.com/token','auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs','client_x509_cert_url': 'https://www.googleapis.com/robot/v1/metadata/x509/angels-of-angela%40curious-clone-258512.iam.gserviceaccount.com'})
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)


# recognize speech using Google Cloud Speech
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
try:
    print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=SPEECH_JSON, language="es-ES"))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
