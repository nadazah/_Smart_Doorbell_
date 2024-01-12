document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('notification-container');

    // Coordonnées actuelles de l'application PWA (à titre d'exemple)
    const cameraCoordinates = { latitude: 37.7749, longitude: -122.4194 }; 

    // Connectez-vous au serveur WebSocket
    const socket = new WebSocket('ws://localhost:8080/pushes');

    // Gérez les événements de connexion WebSocket
    socket.addEventListener('open', (event) => {
        console.log('Connexion WebSocket établie');
    });

    // Gérez les messages WebSocket entrants
    socket.addEventListener('message', (event) => {
        const data = JSON.parse(event.data);

        // Décomposez les données du message
        const { id, image, resultat, date, cameraCoordinates } = data;

        const currentAppCoordinates = await getCurrentCoordinates();


        // Calculez la distance entre les coordonnées actuelles de l'application et les coordonnées de la caméra
        const distance = calculateDistance(currentAppCoordinates, cameraCoordinates);

        // Affichez la notification uniquement si la distance est supérieure à 10m
        if (distance > 10) {
            // Afficher la notification avec la question
            afficherNotification(id, image, resultat, date);
        }
    });

    // ... (restez inchangé)

    // Fonction pour calculer la distance entre deux coordonnées
    function calculateDistance(coord1, coord2) {
        const lat1 = coord1.latitude;
        const lon1 = coord1.longitude;
        const lat2 = coord2.latitude;
        const lon2 = coord2.longitude;

        const R = 6371; // Rayon de la Terre en kilomètres
        const dLat = deg2rad(lat2 - lat1);
        const dLon = deg2rad(lon2 - lon1);

        const a =
            Math.sin(dLat / 2) * Math.sin(dLat / 2) +
            Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) *
            Math.sin(dLon / 2) * Math.sin(dLon / 2);

        const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

        const distance = R * c; // Distance en kilomètres

        return distance;
    }

    function deg2rad(deg) {
        return deg * (Math.PI / 180);
    }

    // Fonction pour obtenir les coordonnées géographiques actuelles
    async function getCurrentCoordinates() {
        return new Promise((resolve, reject) => {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const { latitude, longitude } = position.coords;
                    resolve({ latitude, longitude });
                },
                (error) => {
                    console.error('Erreur de géolocalisation:', error);
                    reject(error);
                }
            );
        });
    }
});
