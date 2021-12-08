# Name: Casey Levy
# CS 362 - HW1 - Credit Card Validator
# Description: Tests for credit_card_validator function
# Test code inspired from HW1 Canvas page:
# https://canvas.oregonstate.edu/courses/1810943/assignments/8334616?module_item_id=20728335
# Credit Card numbers generated from https://www.getcreditcardnumbers.com/
# Numbers validated through https://www.dcode.fr/luhn-algorithm

from credit_card_validator import credit_card_validator
import unittest


class TestCase(unittest.TestCase):

    # Testing Visa prefix only
    # Selected using Category Partition Testing
    def test_1(self):
        self.assertFalse(credit_card_validator("4"))

    # Testing MasterCard prefix only
    # Selected using Category Partition Testing
    def test_2(self):
        self.assertFalse(credit_card_validator("51"))

    # Testing MasterCard prefix only
    # Selected using Category Partition Testing
    def test_3(self):
        self.assertFalse(credit_card_validator("52"))

    # Testing MasterCard prefix only
    # Selected using Category Partition Testing
    def test_4(self):
        self.assertFalse(credit_card_validator("53"))

    # Testing MasterCard prefix only
    # Selected using Category Partition Testing
    def test_5(self):
        self.assertFalse(credit_card_validator("54"))

    # Testing MasterCard prefix only
    # Selected using Category Partition Testing
    def test_6(self):
        self.assertFalse(credit_card_validator("55"))

    # Testing Amex prefix only
    # Selected using Category Partition Testing
    def test_7(self):
        self.assertFalse(credit_card_validator("34"))

    # Testing Amex prefix only
    # Selected using Category Partition Testing
    def test_8(self):
        self.assertFalse(credit_card_validator("37"))

    # Testing MasterCard prefix only
    # Selected using Category Partition Testing
    def test_9(self):
        self.assertFalse(credit_card_validator("2221"))

    # Testing MasterCard prefix only
    # Selected using Category Partition Testing
    def test_10(self):
        self.assertFalse(credit_card_validator("2720"))

    # Prefix of 4, length of 15
    # Selected using Category Partition
    def test_11(self):
        self.assertFalse(credit_card_validator("454487638471755"))

    # Prefix of 51, length of 15
    # Selected using Category Partition
    def test_12(self):
        self.assertFalse(credit_card_validator("512104850406019"))

    # Prefix of 52, length of 15
    # Selected using Category Partition
    def test_13(self):
        self.assertFalse(credit_card_validator("525311694610004"))

    # Prefix of 53, length of 15
    # Selected using Category Partition
    def test_14(self):
        self.assertFalse(credit_card_validator("537207170760089"))

    # Prefix of 54, length of 15
    # Selected using Category Partition
    def test_15(self):
        self.assertFalse(credit_card_validator("546247602570077"))

    # Prefix of 55, length of 15
    # Selected using Category Partition
    def test_16(self):
        self.assertFalse(credit_card_validator("555265620300150"))

    # Prefix of 34, length of 15
    # Selected using Category Partition
    def test_17(self):
        self.assertTrue(credit_card_validator("345026874741365"))

    # Prefix of 37, length of 15
    # Selected using Category Partition
    def test_18(self):
        self.assertTrue(credit_card_validator("378153465667906"))

    # Prefix of 2221, length of 15
    # Selected using Category Partition
    def test_19(self):
        self.assertFalse(credit_card_validator("222175801430077"))

    # Prefix of 2720, length of 15
    # Selected using Category Partition
    def test_20(self):
        self.assertFalse(credit_card_validator("272075808430113"))

    # Prefix of 4, length of 16
    # Selected using Category Partition
    def test_21(self):
        self.assertTrue(credit_card_validator("4929838556906637"))

    # Prefix of 51, length of 16
    # Selected using Category Partition
    def test_22(self):
        self.assertTrue(credit_card_validator("5114249012549171"))

    # Prefix of 52, length of 16
    # Selected using Category Partition
    def test_23(self):
        self.assertTrue(credit_card_validator("5208532531334598"))

    # Prefix of 53, length of 16
    # Selected using Category Partition
    def test_24(self):
        self.assertTrue(credit_card_validator("5310968069648881"))

    # Prefix of 54, length of 16
    # Selected using Category Partition
    def test_25(self):
        self.assertTrue(credit_card_validator("5415568168911372"))

    # Prefix of 55, length of 16
    # Selected using Category Partition
    def test_26(self):
        self.assertTrue(credit_card_validator("5576686566086715"))

    # Prefix of 34, length of 16
    # Selected using Category Partition
    def test_27(self):
        self.assertFalse(credit_card_validator("340358615569044"))

    # Prefix of 37, length of 16
    # Selected using Category Partition
    def test_28(self):
        self.assertFalse(credit_card_validator("372234397274429"))

    # Prefix of 2221, length of 16
    # Selected using Category Partition
    def test_29(self):
        self.assertTrue(credit_card_validator("2221572306540086"))

    # Prefix of 2720, length of 16
    # Selected using Category Partition
    def test_30(self):
        self.assertTrue(credit_card_validator("2720856478020118"))

    # Prefix of 4, length of 14
    # Selected using Category Partition
    def test_31(self):
        self.assertFalse(credit_card_validator("49652378120191"))

    # Prefix of 51, length of 14
    # Selected using Category Partition
    def test_32(self):
        self.assertFalse(credit_card_validator("51478902540109"))

    # Prefix of 52, length of 14
    # Selected using Category Partition
    def test_33(self):
        self.assertFalse(credit_card_validator("52367415890045"))

    # Prefix of 53, length of 14
    # Selected using Category Partition
    def test_34(self):
        self.assertFalse(credit_card_validator("53367415890143"))

    # Prefix of 54, length of 14
    # Selected using Category Partition
    def test_35(self):
        self.assertFalse(credit_card_validator("54723415890047"))

    # Prefix of 55, length of 14
    # Selected using Category Partition
    def test_36(self):
        self.assertFalse(credit_card_validator("55673415890100"))

    # Prefix of 34, length of 14
    # Selected using Category Partition
    def test_37(self):
        self.assertFalse(credit_card_validator("34526780120063"))

    # Prefix of 37, length of 14
    # Selected using Category Partition
    def test_38(self):
        self.assertFalse(credit_card_validator("37524039800087"))

    # Prefix of 2221, length of 14
    # Selected using Category Partition
    def test_39(self):
        self.assertFalse(credit_card_validator("22219657410106"))

    # Prefix of 2720, length of 14
    # Selected using Category Partition
    def test_40(self):
        self.assertFalse(credit_card_validator("27209657410284"))

    # Prefix of 4, length of 17
    # Selected using Category Partition
    def test_41(self):
        self.assertFalse(credit_card_validator("47802357964010057"))

    # Prefix of 51, length of 17
    # Selected using Category Partition
    def test_42(self):
        self.assertFalse(credit_card_validator("51368357964010378"))

    # Prefix of 52, length of 17
    # Selected using Category Partition
    def test_43(self):
        self.assertFalse(credit_card_validator("52370357964010091"))

    # Prefix of 53, length of 17
    # Selected using Category Partition
    def test_44(self):
        self.assertFalse(credit_card_validator("5385703546980106"))

    # Prefix of 54, length of 17
    # Selected using Category Partition
    def test_45(self):
        self.assertFalse(credit_card_validator("5473603546980127"))

    # Prefix of 55, length of 17
    # Selected using Category Partition
    def test_46(self):
        self.assertFalse(credit_card_validator("5574303546980064"))

    # Prefix of 2221, length of 17
    # Selected using Category Partition
    def test_47(self):
        self.assertFalse(credit_card_validator("22217586034800087"))

    # Prefix of 2720, length of 17
    # Selected using Category Partition
    def test_48(self):
        self.assertFalse(credit_card_validator("27203486034800333"))

    # Testing for empty string
    # Selected using Category Partition Testing
    def test_49(self):
        self.assertFalse(credit_card_validator(""))

    # Prefix of 34, length 17
    # Selected using Category Partition
    def test_50(self):
        self.assertFalse(credit_card_validator("34526785014060057"))

    # Prefix of 37, length 17
    # Selected using Category Partition
    def test_51(self):
        self.assertFalse(credit_card_validator("37524030894700182"))

    # Prefix of 4, length of 16, incorrect check digit
    # Selected using Category Partition
    def test_52(self):
        self.assertFalse(credit_card_validator("4532902446535160"))

    # Prefix of 51, length of 16, incorrect check digit
    # Selected using Category Partition
    def test_53(self):
        self.assertFalse(credit_card_validator("5135871924932387"))

    # Prefix of 52, length of 16, incorrect check digit
    # Selected using Category Partition
    def test_54(self):
        self.assertFalse(credit_card_validator("5264703185490106"))

    # Prefix of 53, length of 16, incorrect check digit
    # Selected using Category Partition
    def test_55(self):
        self.assertFalse(credit_card_validator("5368703185490211"))

    # Prefix of 54, length of 16, incorrect check digit
    # Selected using Category Partition
    def test_56(self):
        self.assertFalse(credit_card_validator("5478033185490235"))

    # Prefix of 55, length of 16, incorrect check digit
    # Selected using Category Partition
    def test_57(self):
        self.assertFalse(credit_card_validator("5578013524980071"))

    # Prefix of 34, length of 15, incorrect check digit
    # Selected using Category Partition
    def test_58(self):
        self.assertFalse(credit_card_validator("345278013950017"))

    # Prefix of 37, length of 15, incorrect check digit
    # Selected using Category Partition
    def test_59(self):
        self.assertFalse(credit_card_validator("378501648500075"))

    # Prefix of 2221, length of 16, incorrect check digit
    # Selected using Category Partition
    def test_60(self):
        self.assertFalse(credit_card_validator("2221856703150109"))

    # Prefix of 2720, length of 16, incorrect check digit
    # Selected using Category Partition
    def test_61(self):
        self.assertFalse(credit_card_validator("2720358703150226"))

    # Prefix of 3, length of 16
    # Selected using Category Partition
    def test_62(self):
        self.assertFalse(credit_card_validator("3685046870520003"))

    # Prefix of 50, length of 16
    # Selected using Category Partition
    def test_63(self):
        self.assertFalse(credit_card_validator("5032746870520193"))

    # Prefix of 56, length of 16
    # Selected using Category Partition
    def test_64(self):
        self.assertFalse(credit_card_validator("5683046870520190"))

    # Prefix of 2220, length of 16
    # Selected using Category Partition
    def test_65(self):
        self.assertFalse(credit_card_validator("2220535874150225"))

    # Prefix of 2721, length of 16
    # Selected using Category Partition
    def test_66(self):
        self.assertFalse(credit_card_validator("2721467870520140"))

    # Prefix of 33, length of 15
    # Selected using Category Partition
    def test_67(self):
        self.assertFalse(credit_card_validator("335682014750120"))

    # Prefix of 38, length of 15
    # Selected using Category Partition
    def test_68(self):
        self.assertFalse(credit_card_validator("385607014750191"))

    # Prefix of 35, length of 15
    # Selected using Category Partition
    def test_69(self):
        self.assertFalse(credit_card_validator("357419014750211"))

    # Prefix of 36, length of 15
    # Selected using Category Partition
    def test_70(self):
        self.assertFalse(credit_card_validator("365201014750197"))

    # Prefix of 3, length of 17
    # Selected using Category Partition
    def test_71(self):
        self.assertFalse(credit_card_validator("36850468705200032"))

    # Prefix of 50, length of 17
    # Selected using Category Partition
    def test_72(self):
        self.assertFalse(credit_card_validator("50327468704520193"))

    # Prefix of 56, length of 17
    # Selected using Category Partition
    def test_73(self):
        self.assertFalse(credit_card_validator("56830468170520190"))

    # Prefix of 2220, length of 17
    # Selected using Category Partition
    def test_74(self):
        self.assertFalse(credit_card_validator("22205635874150225"))

    # Prefix of 2721, length of 17
    # Selected using Category Partition
    def test_75(self):
        self.assertFalse(credit_card_validator("27214678705210140"))

    # Prefix of 33, length of 16
    # Selected using Category Partition
    def test_76(self):
        self.assertFalse(credit_card_validator("3356820141750120"))

    # Prefix of 38, length of 16
    # Selected using Category Partition
    def test_77(self):
        self.assertFalse(credit_card_validator("3856070145750191"))

    # Prefix of 35, length of 16
    # Selected using Category Partition
    def test_78(self):
        self.assertFalse(credit_card_validator("3574190147509211"))

    # Prefix of 36, length of 16
    # Selected using Category Partition
    def test_79(self):
        self.assertFalse(credit_card_validator("3652010124750197"))

    # Prefix of 3, length of 15
    # Selected using Category Partition
    def test_80(self):
        self.assertFalse(credit_card_validator("368504605200032"))

    # Prefix of 50, length of 15
    # Selected using Category Partition
    def test_81(self):
        self.assertFalse(credit_card_validator("503274604520193"))

    # Prefix of 56, length of 15
    # Selected using Category Partition
    def test_82(self):
        self.assertFalse(credit_card_validator("568304670520190"))

    # Prefix of 2220, length of 15
    # Selected using Category Partition
    def test_83(self):
        self.assertFalse(credit_card_validator("222056374150225"))

    # Prefix of 2721, length of 15
    # Selected using Category Partition
    def test_84(self):
        self.assertFalse(credit_card_validator("272146787010140"))

    # Prefix of 33, length of 14
    # Selected using Category Partition
    def test_85(self):
        self.assertFalse(credit_card_validator("33568201450120"))

    # Prefix of 38, length of 14
    # Selected using Category Partition
    def test_86(self):
        self.assertFalse(credit_card_validator("38560701750191"))

    # Prefix of 35, length of 14
    # Selected using Category Partition
    def test_87(self):
        self.assertFalse(credit_card_validator("35741907509211"))

    # Prefix of 36, length of 14
    # Selected using Category Partition
    def test_88(self):
        self.assertFalse(credit_card_validator("36520101250197"))

    # Prefix of 2221, length of 15
    # Selected using Category Partition
    def test_89(self):
        self.assertFalse(credit_card_validator("222175801430079"))

    # Prefix of 51, length of 15, incorrect check digit
    # Selected using Category Partition
    def test_90(self):
        self.assertFalse(credit_card_validator("513587924932387"))

    # Prefix of 55, length of 15, incorrect check digit
    # Selected using Category Partition
    def test_91(self):
        self.assertFalse(credit_card_validator("557801324980071"))

    # Prefix of 2221, length of 15, incorrect check digit
    # Selected using Category Partition
    def test_92(self):
        self.assertFalse(credit_card_validator("222175930650067"))

    # Prefix of 2720, length of 15, incorrect check digit
    # Selected using Category Partition
    def test_93(self):
        self.assertFalse(credit_card_validator("272035741590119"))

    # Prefix of 4, length of 15, incorrect check digit
    # Selected using Category Partition
    def test_94(self):
        self.assertFalse(credit_card_validator("457206741590093"))

    # Prefix of 34, length of 14, incorrect check digit
    # Selected using Category Partition
    def test_95(self):
        self.assertFalse(credit_card_validator("34520784500089"))

    # Prefix of 37, length of 14, incorrect check digit
    # Selected using Category Partition
    def test_96(self):
        self.assertFalse(credit_card_validator("37524804500087"))

    # Prefix of 51, length of 17, incorrect check digit
    # Selected using Category Partition
    def test_97(self):
        self.assertFalse(credit_card_validator("51328703649850045"))

    # Prefix of 55, length of 17, incorrect check digit
    # Selected using Category Partition
    def test_98(self):
        self.assertFalse(credit_card_validator("55637804649850060"))

    # Prefix of 2221, length of 17, incorrect check digit
    # Selected using Category Partition
    def test_99(self):
        self.assertFalse(credit_card_validator("22217539514080109"))

    # Prefix of 2720, length of 17, incorrect check digit
    # Selected using Category Partition
    def test_100(self):
        self.assertFalse(credit_card_validator("27204389514080035"))

    # Prefix of 4, length of 17, incorrect check digit
    # Selected using Category Partition
    def test_101(self):
        self.assertFalse(credit_card_validator("47502863571040090"))

    # Prefix of 34, length of 16, incorrect check digit
    # Selected using Category Partition
    def test_102(self):
        self.assertFalse(credit_card_validator("3452706890470068"))

    # Prefix of 37, length of 16, incorrect check digit
    # Selected using Category Partition
    def test_103(self):
        self.assertFalse(credit_card_validator("3741806590470125"))


if __name__ == '__main__':
    unittest.main()
