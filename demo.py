    def _do_roll(self, num_dice):
        values = []

        for i in range(num_dice):
            dice_val = random.randint(1,6)
            values.append(dice_val)
        return values

        return [random.randint(1.6) for i in range(num_dice)]

        return tuple(random.randint(1.6) for _ in range(num_dice))  #tavsiye edilmiyor

        # yukaridaki ucu ayni farkli yazim. fotografta testi var.
