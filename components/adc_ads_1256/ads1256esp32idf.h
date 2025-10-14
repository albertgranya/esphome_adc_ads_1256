#pragma once

#ifdef USE_ESP_IDF

#include "adc_ads_1256.h"

namespace esphome {
namespace adc_ads_1256 {

class ADCADS1256ESP32IDF : public ADCADS1256 {
 public:
  ADCADS1256ESP32IDF() = default;

  void send_break() override;

  void set_uart_num(int num) override {
    this->uart_idx_ = num;
  }
};

}  // namespace adc_ads_1256
}  // namespace esphome

#endif  // USE_ESP_IDF
