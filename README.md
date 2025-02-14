# BMI/BMR API

This API provides calculations for:
- **Body Mass Index (BMI)**
- **Basal Metabolic Rate (BMR)**

## 📌 Technologies Used
- [FastAPI](https://fastapi.tiangolo.com/) - for building the API.
- [Pydantic](https://pydantic-docs.helpmanual.io/) - for data validation.
- [Uvicorn](https://www.uvicorn.org/) - as the ASGI server.
- [Docker](https://www.docker.com/) - for containerization.
- [GitHub Actions](https://github.com/features/actions) - for CI/CD.
- [Azure Web Apps](https://azure.microsoft.com/en-us/products/app-service/web) - for cloud deployment.
- **Makefile** for automation of setup, testing, and deployment tasks.

---
## 🔧 Installation and Usage

### 🛠 Makefile Commands

The Makefile automates common tasks for easier project management. Below are the available commands:

- `make init` - Installs dependencies.
- `make run` - Starts the FastAPI server locally.
- `make test` - Runs the test suite using `pytest`.
- `make build` - Builds a Docker image for the application.
- `make deploy` - Deploys the latest containerized version of the API.

To simplify deployment, there are two commands that deploy locally or with the latest containerized version:
- `make local` - Initiates dependancies, runs tests and deploys locally
- `make docker` - Runs tests, builds image and deploys the latest containerized version of the API.

### 🚀 Local Deployment

1. **Clone the repository:**
```bash
git clone <repository-url>
cd <repository-name>
```

2. **Initialize the project using Makefile:**
```bash
make local
```

---
## 🐳 Running with Docker (Containerization)

1. **Build and run the Docker image:**
```bash
make docker
```
---
## ☁️ Deploying to Azure

### **How the Azure Deployment Works**

The deployment process is managed via **GitHub Actions** and **Azure Web Apps**:
1. **GitHub Actions Workflow:**
   - On push to `main`, GitHub Actions triggers the pipeline.
   - The Docker image is built and pushed to **GitHub Container Registry (GHCR)**.
   - Azure Web App pulls the latest container image from GHCR.

2. **Azure Connection & Authentication:**
   - The workflow logs into Azure using secrets stored in GitHub (`AZUREAPPSERVICE_CLIENTID`, `AZUREAPPSERVICE_TENANTID`, etc.).
   - It updates the App Service to use the latest Docker image.
   - Finally, it restarts the web app to apply the changes.

### **Deployment Steps**
1. **Ensure you have an Azure Web App set up** and connected to **GitHub Repository** (in the Deployment Center).

Once you run the CI/CD pipeline, the step **Build and push Docker image** will add it to the registry and Azure will be able to pull it. 

```yaml
- name: Login to GitHub Container Registry
  uses: docker/login-action@v2
  with:
    registry: ghcr.io
    username: ${{ github.repository_owner }}
    password: ${{ secrets.GITHUB_TOKEN }}

- name: Build and push Docker image
  uses: docker/build-push-action@v3
  with:
    context: .
    file: ./Dockerfile
    push: true
    tags: ghcr.io/${{ env.lower_owner }}/${{ secrets.AZURE_WEBAPP_NAME }}:latest

```

2. **GitHub Secrets Configuration** (needed for authentication):
   - `AZUREAPPSERVICE_CLIENTID`
   - `AZUREAPPSERVICE_TENANTID`
   - `AZUREAPPSERVICE_SUBSCRIPTIONID`
   - `AZUREAPPSERVICE_PUBLISHPROFILE`
   - `AZURE_WEBAPP_NAME`
   - `AZURE_RESOURCE_GROUP_NAME`

The `AZUREAPPSERVICE` variables are created automatically when linking the App Service; however, the last two variables must be added manually in the GitHub Secrets configuration (Settings > Security > Secrets and variables > Actions > Repository Secrets)

3. **Run the pipeline te deploy the Azure Web App**
You should then be able to see your beautiful API! 
> You should be able to get the URL from Azure App Service.

---
## ✅ Running Tests

You can run the test suite using Makefile:
```bash
make test
```

---
## 🛠 Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| POST   | `/bmi`  | Calculate Body Mass Index |
| POST   | `/bmr`  | Calculate Basal Metabolic Rate |

### Example Request (BMI Calculation)
```json
{
    "height": 175,
    "weight": 70
}
```
From a CLI, the command would be:
```bash
curl -X POST http://<url>:9000/bmi \
     -H "Content-Type: application/json" \
     -d '{"height": 175, "weight": 70}'
```

### Example Response
```json
{
    "bmi": 22.86,
    "category": "Normal weight"
}
```
From a CLI, the command would be:
```bash
curl -X POST http://<url>:9000/bmi \
     -H "Content-Type: application/json" \
     -d '{"age": 30, "gender": "male", "height": 175, "weight": 70}'
```
