import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import spi
from esphome.core import CORE
from esphome import pins

from esphome.const import CONF_ID,CONF_MOSI_PIN,CONF_MISO_PIN
from esphome.const import CONF_DRDY_PIN, CONF_RESET_PIN,CONF_CHIP_SELECT_PIN
from esphome.const import CONF_SS_PIN,CONF_VREF, CONF_CLOCK_MHZ

CODEOWNERS = ['@albertgranya']

DEPENDENCIES = ['spi','output']
MULTI_CONF = True


adc_ads_1256_ns = cg.esphome_ns.namespace("adc_ads_1256")
ADCADS1256 = adc_ads_1256_ns.class_(
    "ADCADS1256", cg.Component, spi.SPIDevice
)
ADCADS1256ESP32IDF = adc_ads_1256_ns.class_('ADCADS1256ESP32IDF', cg.Component)

def _declare_type(value):
    if CORE.is_esp32:
        if CORE.using_esp_idf:
            return cv.declare_id(ADCADS1256ESP32IDF)(value)

    raise NotImplementedError


CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): _declare_type,
    cv.Optional(CONF_MOSI_PIN, default=18): pins.gpio_output_pin_schema,
    cv.Optional(CONF_MISO_PIN, default=19): pins.gpio_input_pin_schema,
    cv.Optional(CONF_SS_PIN, default=21): pins.gpio_output_pin_schema,
    cv.Optional(CONF_VREF, default=2.5): cv.float_,
    cv.Optional(CONF_CLOCK_MHZ, default=7.68): cv.float_,
    cv.Optional(CONF_DRDY_PIN, default=20): pins.gpio_input_pin_schema,
    cv.Optional(CONF_RESET_PIN, default=22): pins.gpio_output_pin_schema,
    cv.Optional(CONF_CHIP_SELECT_PIN, default=23): pins.gpio_output_pin_schema,
}).extend(cv.COMPONENT_SCHEMA).extend(spi.SPIDeviceSchema)



async def to_code(config):
    cg.add_global(adc_ads_1256_ns.using)
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await spi.register_spi_device(var, config)
     
    if CONF_MOSI_PIN in config:
        mosi = await cg.gpio_pin_expression(config[CONF_MOSI_PIN])
        cg.add(var.set_mosi_pin(mosi))
    if CONF_MISO_PIN in config:
        miso = await cg.gpio_pin_expression(config[CONF_MISO_PIN])
        cg.add(var.set_miso_pin(miso))
    if CONF_SS_PIN in config:
        ss = await cg.gpio_pin_expression(config[CONF_SS_PIN])
        cg.add(var.set_ss_pin(ss))
    if CONF_VREF in config:
        cg.add(var.set_vref(config[CONF_VREF]))
    if CONF_CLOCK_MHZ in config:
        cg.add(var.set_clockMHZ(config[CONF_CLOCK_MHZ]))
    if CONF_DRDY_PIN in config:
        drdy = await cg.gpio_pin_expression(config[CONF_DRDY_PIN])
        cg.add(var.set_drdy_pin(drdy))
    if CONF_RESET_PIN in config:
        reset = await cg.gpio_pin_expression(config[CONF_RESET_PIN])
        cg.add(var.set_reset_pin(reset))
    if CONF_CHIP_SELECT_PIN in config:
        cs = await cg.gpio_pin_expression(config[CONF_CHIP_SELECT_PIN])
        cg.add(var.set_chip_select_pin(cs))
    







