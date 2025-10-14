#include "esphome/core/log.h"
#include "adc_ads_1256.h"

namespace esphome {
namespace adc_ads_1256 {

static const char *TAG = "adc_ads_1256";

void ADCADS1256::setup() {

}

void ADCADS1256::loop() {

}

void ADCADS1256::dump_config(){
    ESP_LOGCONFIG(TAG, "Empty SPI component");
}

}  // namespace adc_ads_1256
}  // namespace esphome
