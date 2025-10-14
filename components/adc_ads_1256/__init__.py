import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import spi
from esphome.const import CONF_ID
from esphome.const import CONF_TX_PIN, CONF_ENABLE_PIN, CONF_UPDATE_INTERVAL, CONF_PERIODIC_UPDATE, CONF_FORCE_FULL_FRAMES
from esphome.const import CONF_MOSI_PIN,CONF_MISO_PIN,CONF_SS_PIN,CONF_VREF, CONF_CLOCK_MHZ,CONF_DRDY_PIN, CONF_RESET_PIN,CONF_CHIP_SELECT_PIN
DEPENDENCIES = ["spi"]

adc_ads_1256_ns = cg.esphome_ns.namespace("adc_ads_1256")
ADCADS1256 = adc_ads_1256_ns.class_(
    "ADCADS1256", cg.Component, spi.SPIDevice
)


CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): _declare_type,
    cv.Optional(CONF_MOSI_PIN, default=18): pins.gpio_output_pin_schema,
    cv.Optional(CONF_MISO_PIN, default=19): pins.gpio_input_pin_schema,
    cv.Optional(CONF_SS_PIN, default=21): pins.gpio_output_pin_schema,
    cv.Optional(CONF_VREF, default=2.5): cv.float_,
    cv.Optional(CONF_CLOCK_MHZ, default=7.68): cv.float_,
    cv.Optional(CONF_DRDY_PIN, default=20): pins.gpio_input_pin_schema,
    cv.Optional(CONF_RESET_PIN, default=22): pins.gpio_output_pin_schema,
    cv.Optional(CONF_CHIP_SELECT_PIN, default=21): pins.gpio_output_pin_schema,

    # cv.Optional(CONF_ENABLE_PIN): pins.gpio_output_pin_schema,
    # cv.Optional(CONF_TX_PIN, default=5): pins.internal_gpio_output_pin_schema,
    # cv.Optional(CONF_UART_NUM, default=1): cv.int_range(min=0, max=UART_MAX),
    # cv.Optional(CONF_PERIODIC_UPDATE, default=True): cv.boolean,
    # cv.Optional(CONF_FORCE_FULL_FRAMES, default=False): cv.boolean,
    # cv.Optional(CONF_CUSTOM_MAB_LEN, default=12): cv.int_range(min=12, max=1000),
    # cv.Optional(CONF_CUSTOM_BREAK_LEN, default=92): cv.int_range(min=92, max=1000),
    # cv.Optional(CONF_UPDATE_INTERVAL, default=500): cv.int_range(),
}).extend(cv.COMPONENT_SCHEMA).extend(uart.UART_DEVICE_SCHEMA)



async def to_code(config):
    cg.add_global(adc_ads_1256_ns.using)
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    # await uart.register_uart_device(var, config)
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
    
    

    # if CONF_ENABLE_PIN in config:
    #     enable = await cg.gpio_pin_expression(config[CONF_ENABLE_PIN])
    #     cg.add(var.set_enable_pin(enable))

    # if CONF_TX_PIN in config:
    #     tx_pin = await cg.gpio_pin_expression(config[CONF_TX_PIN])
    #     cg.add(var.set_uart_tx_pin(tx_pin))

    # cg.add(var.set_uart_num(config[CONF_UART_NUM]))
    # cg.add(var.set_periodic_update(config[CONF_PERIODIC_UPDATE]))
    # cg.add(var.set_force_full_frames(config[CONF_FORCE_FULL_FRAMES]))
    # cg.add(var.set_mab_len(config[CONF_CUSTOM_MAB_LEN]))
    # cg.add(var.set_break_len(config[CONF_CUSTOM_BREAK_LEN]))
    # cg.add(var.set_update_interval(config[CONF_UPDATE_INTERVAL]))

