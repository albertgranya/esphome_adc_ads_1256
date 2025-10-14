#ifdef USE_ESP_IDF

#include "ads1256esp32idf.h"
#include "esphome/core/log.h"
#include <driver/uart.h>

namespace esphome {
namespace adc_ads_1256 {

static const char *TAG = "adc_ads_1256";

void ads1256esp32idf::send_break() {
  uart_set_line_inverse((uart_port_t)this->uart_idx_, UART_SIGNAL_TXD_INV);
  delayMicroseconds(this->break_len_);
  uart_set_line_inverse((uart_port_t)this->uart_idx_, UART_SIGNAL_INV_DISABLE);
  delayMicroseconds(this->mab_len_);
}

}  // namespace adc_ads_1256
}  // namespace esphome
#endif  // USE_ESP_IDF
