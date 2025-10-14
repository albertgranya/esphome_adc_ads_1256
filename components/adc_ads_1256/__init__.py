import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import spi
from esphome.const import CONF_ID

DEPENDENCIES = ["spi"]

adc_ads_1256_ns = cg.esphome_ns.namespace("adc_ads_1256")
ADCADS1256 = adc_ads_1256_ns.class_(
    "ADCADS1256", cg.Component, spi.SPIDevice
)

# sck_pin: 9
#    mosi_pin: 18
#    miso_pin: 19   
#    ss_pin: 21
   
#    vRef: 2.5
#    clockMHZ: 7.68
   
#    drdy_pin: 20
#    reset_pin: 22
#    chip_select_pin: 21

CONFIG_SCHEMA = (
    cv.Schema({cv.GenerateID(): cv.declare_id(ADCADS1256)})
    .extend(cv.COMPONENT_SCHEMA)
    .extend(spi.spi_device_schema(sck_pin_required=True)
    .extend({
        cv.Optional("mosi_pin"): cv.all(cv.int_, cv.Range(0, 39)),
        cv.Optional("miso_pin"): cv.all(cv.int_, cv.Range(0, 39)),
        cv.Optional("ss_pin"): cv.all(cv.int_, cv.Range(0, 39)),
        cv.Optional("vRef"): cv.float_,
        cv.Optional("clockMHZ"): cv.float_,
        cv.Optional("drdy_pin"): cv.all(cv.int_, cv.Range(0, 39)),
        cv.Optional("reset_pin"): cv.all(cv.int_, cv.Range(0, 39)),
        cv.Optional("chip_select_pin"): cv.all(cv.int_, cv.Range(0, 39)),
    })
    
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await spi.register_spi_device(var, config)
