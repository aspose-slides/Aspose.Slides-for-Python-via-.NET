from aspose.slides.animation import EffectType


def animation_float_up_down():
    effect_type = EffectType.DESCEND
    print(effect_type == EffectType.DESCEND) # Should return 'True'
    print(effect_type == EffectType.FLOAT_DOWN) # Should return 'True'

    effect_type = EffectType.FLOAT_DOWN
    print(effect_type == EffectType.DESCEND) # Should return 'True'
    print(effect_type == EffectType.FLOAT_DOWN) # Should return 'True'

    effect_type = EffectType.ASCEND
    print(effect_type == EffectType.ASCEND) # Should return 'True'
    print(effect_type == EffectType.FLOAT_UP) # Should return 'True'

    effect_type = EffectType.FLOAT_UP
    print(effect_type == EffectType.ASCEND) # Should return 'True'
    print(effect_type == EffectType.FLOAT_UP) # Should return 'True'
