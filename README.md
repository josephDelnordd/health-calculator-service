# 🩺 Health Calculator Service

Microservice REST en **Python (Flask)** permettant de calculer des indicateurs de santé :
- **BMI (Body Mass Index)**
- **BMR (Basal Metabolic Rate)**

L’application est conteneurisée avec **Docker**, automatisée via **GitHub Actions**, et déployée sur **Azure App Service (Linux / Container)**.

---

## ⚙️ Technologies

- Python 3.9
- Flask
- Docker
- GitHub Actions (CI/CD)
- Docker Hub
- Azure App Service

---

## 🚀 Déploiement

Le pipeline CI/CD :
1. Lance les tests unitaires
2. Construit l’image Docker
3. Publie l’image sur Docker Hub
4. Azure App Service déploie automatiquement la dernière image

---

## 🔗 Endpoints API

### ✅ Health check

- **GET** `/health`
- **Response** : `{"status": "ok"}`

### ✅ BMI

- **POST** `/bmi`
- **Payload** :

```json
{
	"weight": 70,
	"height": 1.75
}
```

### ✅ BMR

- **POST** `/bmr`
- **Payload** :

```json
{
  "height": 175,
  "weight": 70,
  "age": 25,
  "gender": "male"
}
```

---

## 🌍 Application en ligne

L’API est accessible via Azure App Service :
- **URL** : `https://health-calculator-service-<suffix>.azurewebsites.net/health`

