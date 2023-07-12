name="nichollsflaskapp"
resourceGroup="Azuredevops"
runtime="PYTHON|3.7"

# spin up azure application
az webapp up --name $name --runtime $runtime --resource-group $resourceGroup

# show url
az webapp show --name $name --resource-group $resourceGroup --query defaultHostName --output tsv
