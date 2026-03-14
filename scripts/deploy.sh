#!/bash/bin

if [ -z "$IP_VM" ]; then
    echo "Error: The IP_VM variable is not defined."
    exit 1
fi

echo "Initiating the deployment in Azure..."


scp -i $KEY_PATH ../app/app.py $USER_VM@$IP_VM:/home/$USER_VM/mtd_app/app.py

ssh -i $KEY_PATH $USER_VM@$IP_VM "pkill gunicorn; cd mtd_app && source venv/bin/activate && gunicorn --bind 0.0.0.0:8080 app:app --daemon"

echo "update app"
