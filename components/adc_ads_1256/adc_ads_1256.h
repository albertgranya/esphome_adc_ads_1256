#pragma once

#include "esphome/core/component.h"
#include "esphome/components/spi/spi.h"
#include "esphome/components/output/float_output.h"
#include "ADS1256.h"
static const uint16_t UPDATE_INTERVAL_MS = 500;
static const uint16_t DMX_MAX_CHANNEL = 512;
static const uint16_t DMX_MSG_SIZE = DMX_MAX_CHANNEL + 1;
static const int DMX_BREAK_LEN = 92;
static const int DMX_MAB_LEN = 12;
static const int DMX_MIN_INTERVAL_MS = 23;

namespace esphome {
namespace adc_ads_1256 {

class ADCADS1256 : public Component, 
                    public spi::SPIDevice<spi::BIT_ORDER_MSB_FIRST,spi::CLOCK_POLARITY_LOW, 
                            spi::CLOCK_PHASE_LEADING,spi::DATA_RATE_1KHZ> {
  public:
   ADCADS1256() = default;
   void setup() override;
    void loop() override;
    void dump_config() override;
  protected:
    esphome::uart::UARTComponent *uart_{nullptr};
    esphome::ADS1256::ADS1256Component *adc_{nullptr};
// Construct and init ADS1256 object
    //ADS1256 adc(sck,miso,mosi,ss,clockMHZ,vRef,true); // RESETPIN is permanently tied to 3.3v
    std::vector<uint8_t> rx_buffer_;
    uint32_t last_dmx512_transmission_{0};
    uint8_t device_values_[DMX_MSG_SIZE];
    int uart_idx_{0};
    InternalGPIOPin *tx_pin_{nullptr};
    int update_interval_{UPDATE_INTERVAL_MS};
    int mab_len_{DMX_MAB_LEN};
    int break_len_{DMX_BREAK_LEN};
    uint16_t max_chan_{0};
    bool update_{true};
    bool periodic_update_{true};
    bool force_full_frames_{false};
    uint32_t last_update_{0};
    GPIOPin *pin_enable_{nullptr};
    //float vRef = 2.5; // voltage reference
    //float clockMHZ = 7.68; // crystal frequency used on ADS1256
   
    float vRef_{vRef}; // voltage reference
    float clockMHZ_{clockMHZ}; // crystal frequency used on ADS1256

    float vRef_{vRef};
    //int8_t sck=9;
    //int sck_pin_{sck_pin};
    InternalGPIOPin *sck_pin_{nullptr};
    //int8_t miso=19;
    InternalGPIOPin *miso_pin_{nullptr};
    //int8_t mosi=18;
    InternalGPIOPin *mosi_pin_{nullptr};
    //int8_t ss =21;
    InternalGPIOPin *ss_pin_{nullptr};

    // drdy_pin: 20
    InternalGPIOPin *drdy_pin_{nullptr};
    // reset_pin: 22
    InternalGPIOPin *reset_pin_{nullptr};
    // chip_select_pin: 21
    InternalGPIOPin *chip_select_pin_{nullptr};

    float sensor1, sensor2, sensor3, sensor4;
};

class ADS1256Output : public output::FloatOutput, public Component {
public:
  void set_universe(ADS1256 *universe) { this->universe_ = universe; }
  void set_channel(uint16_t channel);
  void write_state(float state) override;
  float state;

protected:
  uint16_t channel_{0};
  ADS1256 *universe_{nullptr};
};
};


}  // namespace adc_ads_1256
}  // namespace esphome
