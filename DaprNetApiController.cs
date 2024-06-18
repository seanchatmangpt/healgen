
    using Microsoft.AspNetCore.Mvc;
    using Dapr.Client;
    using System.Threading.Tasks;

    namespace DaprNetApi.Controllers
    {
        [ApiController]
        [Route("[controller]")]
        public class WeatherForecastController : ControllerBase
        {
            private readonly DaprClient _daprClient;

            public WeatherForecastController(DaprClient daprClient)
            {
                _daprClient = daprClient;
            }

            [HttpPost("weatherupdates")]
            public async Task<IActionResult> GetWeatherUpdates([FromBody] WeatherForecast forecast)
            {
                // Process the message
                await Task.Yield(); // Placeholder for actual processing logic

                return Ok();
            }
        }

        public class WeatherForecast
        {
            public DateTime Date { get; set; }
            public int TemperatureC { get; set; }
            public string Summary { get; set; }
        }
    }
    