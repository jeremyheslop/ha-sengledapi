from custom_components.sengledapi.sengledapi.devices.bulbs.bulb import Bulb


def test_convert_color_ha():
    bulb = Bulb(
        api=None,
        device_mac="00:11:22:33:44:55",
        friendly_name="Test",
        state=False,
        device_model="model",
        isonline=True,
        support_color=True,
        support_color_temp=True,
        support_brightness=True,
        jsession_id="",
        country="us",
        wifi=False,
    )
    result = bulb.convert_color_HA((255, 128, 0))
    assert result == "255:128:0"

