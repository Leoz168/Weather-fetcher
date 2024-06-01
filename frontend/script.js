async function getWeather() {
    const city = document.getElementById('cityInput').value;
    console.log(`Fetching weather for city: ${city}`);

    try {
        const response = await fetch(`http://localhost:5000/weather?city=${city}`);
        console.log('Response:', response);

        if (response.ok) {
            const data = await response.json();
            console.log('Data:', data);

            document.getElementById('temperature').innerText = `Temperature: ${data.temp_c.toFixed(2)}˚C or ${data.temp_f.toFixed(2)}˚F`;
            document.getElementById('feelsLike').innerText = `Feels Like: ${data.feels_c.toFixed(2)}˚C or ${data.feels_f.toFixed(2)}˚F`;
            document.getElementById('humidity').innerText = `Humidity: ${data.humidity}%`;
            document.getElementById('windSpeed').innerText = `Wind Speed: ${data.wind_spd} m/s`;
            document.getElementById('description').innerText = `General Weather: ${data.description}`;
            document.getElementById('sunrise').innerText = `Sunrise: ${data.sunrise}`;
            document.getElementById('sunset').innerText = `Sunset: ${data.sunset}`;

            document.getElementById('weatherResult').classList.remove('d-none');
        } else {
            console.error('Error fetching weather data:', response.statusText);
        }
    } catch (error) {
        console.error('Fetch error:', error);
    }
}
