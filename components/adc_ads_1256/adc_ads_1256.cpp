#include "esphome/core/log.h"
#include "adc_ads_1256.h"

namespace esphome {
namespace components{
namespace adc_ads_1256 {
static const char *TAG = "adc_ads_1256";
// Construct and init ADS1256 object
//static ADS1256 adc;//(sck,miso,mosi,ss,clockMHZ,vRef,true); // RESETPIN is permanently tied to 3.3v
ADS1256 adc;//(sck,miso,mosi,ss,clockMHZ,vRef,true);
void ADCADS1256::setup() {
//adc.init();
adc(sck_pin_, miso_pin_, mosi_pin_, ss_pin_, clockMHZ_, vRef_, true);
}


void ADCADS1256::loop() {

}

void ADCADS1256::dump_config(){
    ESP_LOGCONFIG(TAG, "Empty SPI component");
}


// void DMX512::set_channel_used(uint16_t channel) {

// }

// void DMX512::write_channel(uint16_t channel, uint8_t value) {
//   ESP_LOGD(TAG, "write_channel %d: %d", channel, value);

// }

// void DMX512Output::set_channel(uint16_t channel) {
// }

// void DMX512Output::write_state(float state) {
// }


}  // namespace adc_ads_1256
}
}  // namespace esphome

