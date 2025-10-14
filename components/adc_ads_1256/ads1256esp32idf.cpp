#ifdef USE_ESP_IDF

#include "ads1256esp32idf.h"
#include "esphome/core/log.h"
#include <driver/uart.h>

namespace esphome {
namespace adc_ads_1256 {

static const char *TAG = "adc_ads_1256";

void ADCADS1256ESP32IDF::send_break() {

}

}  // namespace adc_ads_1256
}  // namespace esphome
#endif  // USE_ESP_IDF
