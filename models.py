# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ActiveTime(models.Model):
    branchid = models.OneToOneField('Block', models.DO_NOTHING, db_column='BranchID', primary_key=True)  # Field name made lowercase.
    blockid = models.ForeignKey('Block', models.DO_NOTHING, db_column='BlockID', to_field='BlockID')  # Field name made lowercase.
    opentime = models.TimeField(db_column='openTime')  # Field name made lowercase.
    closetime = models.TimeField(db_column='closeTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'active_time'
        unique_together = (('branchid', 'blockid', 'opentime'),)


class BedInfo(models.Model):
    roomid = models.OneToOneField('RoomType', models.DO_NOTHING, db_column='RoomID', primary_key=True)  # Field name made lowercase.
    size = models.DecimalField(db_column='Size', max_digits=2, decimal_places=1)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bed_info'
        unique_together = (('roomid', 'size'),)


class Block(models.Model):
    branchid = models.OneToOneField('Branch', models.DO_NOTHING, db_column='BranchID', primary_key=True)  # Field name made lowercase.
    blockid = models.PositiveIntegerField(db_column='BlockID')  # Field name made lowercase.
    length = models.FloatField(db_column='Length')  # Field name made lowercase.
    width = models.FloatField(db_column='Width')  # Field name made lowercase.
    rentalprice = models.PositiveIntegerField(db_column='RentalPrice')  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    serviceid = models.ForeignKey('Service', models.DO_NOTHING, db_column='ServiceID', blank=True, null=True)  # Field name made lowercase.
    storename = models.CharField(db_column='StoreName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    logo = models.CharField(db_column='Logo', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'block'
        unique_together = (('branchid', 'blockid'),)


class Booking(models.Model):
    bookingid = models.CharField(db_column='BookingID', primary_key=True, max_length=20)  # Field name made lowercase.
    bookingdate = models.DateTimeField(db_column='BookingDate')  # Field name made lowercase.
    guestnum = models.PositiveIntegerField(db_column='GuestNum')  # Field name made lowercase.
    checkin = models.DateTimeField(db_column='CheckIn')  # Field name made lowercase.
    checkout = models.DateTimeField(db_column='CheckOut')  # Field name made lowercase.
    status = models.PositiveIntegerField(db_column='Status')  # Field name made lowercase.
    totalpay = models.PositiveIntegerField(db_column='TotalPay')  # Field name made lowercase.
    customerid = models.ForeignKey('Customer', models.DO_NOTHING, db_column='CustomerID')  # Field name made lowercase.
    packagename = models.ForeignKey('ServicePacket', models.DO_NOTHING, db_column='PackageName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'booking'


class BookingBill(models.Model):
    billid = models.CharField(db_column='BillID', primary_key=True, max_length=20)  # Field name made lowercase.
    checkin = models.TimeField(db_column='CheckIn')  # Field name made lowercase.
    checkout = models.TimeField(db_column='CheckOut')  # Field name made lowercase.
    bookingid = models.ForeignKey(Booking, models.DO_NOTHING, db_column='BookingID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'booking_bill'


class BookingBillSeq(models.Model):

    class Meta:
        managed = False
        db_table = 'booking_bill_seq'


class BookingRoom(models.Model):
    bookingid = models.OneToOneField(Booking, models.DO_NOTHING, db_column='BookingID', primary_key=True)  # Field name made lowercase.
    branchid = models.ForeignKey('Room', models.DO_NOTHING, db_column='BranchID')  # Field name made lowercase.
    roomnumber = models.ForeignKey('Room', models.DO_NOTHING, db_column='RoomNumber', to_field='RoomNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'booking_room'
        unique_together = (('bookingid', 'branchid', 'roomnumber'),)


class BookingSeq(models.Model):

    class Meta:
        managed = False
        db_table = 'booking_seq'


class Branch(models.Model):
    branchid = models.CharField(db_column='BranchID', primary_key=True, max_length=6)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=50)  # Field name made lowercase.
    address = models.CharField(db_column='Address', unique=True, max_length=100)  # Field name made lowercase.
    phonenum = models.CharField(db_column='PhoneNum', unique=True, max_length=12)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'branch'


class BranchSeq(models.Model):

    class Meta:
        managed = False
        db_table = 'branch_seq'


class Customer(models.Model):
    customerid = models.CharField(db_column='CustomerID', primary_key=True, max_length=10)  # Field name made lowercase.
    citizenid = models.CharField(db_column='CitizenID', unique=True, max_length=12)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=45)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', unique=True, max_length=12)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45, blank=True, null=True)  # Field name made lowercase.
    point = models.PositiveIntegerField(db_column='Point', blank=True, null=True)  # Field name made lowercase.
    customertype = models.PositiveIntegerField(db_column='CustomerType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class Enterprise(models.Model):
    enterpriseid = models.CharField(db_column='EnterpriseID', primary_key=True, max_length=8)  # Field name made lowercase.
    enterprisename = models.CharField(db_column='EnterpriseName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'enterprise'


class ImageBranch(models.Model):
    branchid = models.OneToOneField(Branch, models.DO_NOTHING, db_column='BranchID', primary_key=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'image_branch'
        unique_together = (('branchid', 'image'),)


class PacketBill(models.Model):
    customerid = models.OneToOneField(Customer, models.DO_NOTHING, db_column='CustomerID', primary_key=True)  # Field name made lowercase.
    packagename = models.ForeignKey('ServicePacket', models.DO_NOTHING, db_column='PackageName')  # Field name made lowercase.
    purchasedate = models.DateTimeField(db_column='PurchaseDate')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    totalpay = models.IntegerField(db_column='TotalPay', blank=True, null=True)  # Field name made lowercase.
    remainday = models.PositiveIntegerField(db_column='RemainDay', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'packet_bill'
        unique_together = (('customerid', 'packagename', 'purchasedate'),)


class Room(models.Model):
    branchid = models.OneToOneField('Zone', models.DO_NOTHING, db_column='BranchID', primary_key=True)  # Field name made lowercase.
    roomnumber = models.CharField(db_column='RoomNumber', max_length=3)  # Field name made lowercase.
    roomid = models.ForeignKey('RoomType', models.DO_NOTHING, db_column='RoomID')  # Field name made lowercase.
    zonename = models.ForeignKey('Zone', models.DO_NOTHING, db_column='ZoneName', to_field='ZoneName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'room'
        unique_together = (('branchid', 'roomnumber'),)


class RoomType(models.Model):
    roomid = models.AutoField(db_column='RoomID', primary_key=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=45)  # Field name made lowercase.
    area = models.PositiveIntegerField(db_column='Area')  # Field name made lowercase.
    numguest = models.PositiveIntegerField(db_column='NumGuest')  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'room_type'


class RoomTypeSupplyType(models.Model):
    sppid = models.OneToOneField('SupplyType', models.DO_NOTHING, db_column='SppID', primary_key=True)  # Field name made lowercase.
    roomid = models.ForeignKey(RoomType, models.DO_NOTHING, db_column='RoomID')  # Field name made lowercase.
    quantity = models.PositiveIntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'room_type_supply_type'
        unique_together = (('sppid', 'roomid'),)


class RoomtypeBranch(models.Model):
    roomid = models.OneToOneField(RoomType, models.DO_NOTHING, db_column='RoomID', primary_key=True)  # Field name made lowercase.
    branchid = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchID')  # Field name made lowercase.
    rentalprice = models.PositiveIntegerField(db_column='RentalPrice')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roomtype_branch'
        unique_together = (('roomid', 'branchid'),)


class Service(models.Model):
    serviceid = models.CharField(db_column='ServiceID', primary_key=True, max_length=8)  # Field name made lowercase.
    servicetype = models.CharField(db_column='ServiceType', max_length=1)  # Field name made lowercase.
    guestnum = models.PositiveIntegerField(db_column='GuestNum', blank=True, null=True)  # Field name made lowercase.
    style = models.CharField(db_column='Style', max_length=45, blank=True, null=True)  # Field name made lowercase.
    enterpriseid = models.ForeignKey(Enterprise, models.DO_NOTHING, db_column='EnterpriseID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'service'


class ServicePacket(models.Model):
    packagename = models.CharField(db_column='PackageName', primary_key=True, max_length=50)  # Field name made lowercase.
    daynum = models.PositiveIntegerField(db_column='DayNum')  # Field name made lowercase.
    guestnum = models.PositiveIntegerField(db_column='GuestNum')  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'service_packet'


class SouvenirBrand(models.Model):
    serviceid = models.OneToOneField(Service, models.DO_NOTHING, db_column='ServiceID', primary_key=True)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'souvenir_brand'
        unique_together = (('serviceid', 'brand'),)


class SouvenirCategory(models.Model):
    serviceid = models.OneToOneField(Service, models.DO_NOTHING, db_column='ServiceID', primary_key=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'souvenir_category'
        unique_together = (('serviceid', 'category'),)


class SpaService(models.Model):
    serviceid = models.OneToOneField(Service, models.DO_NOTHING, db_column='ServiceID', primary_key=True)  # Field name made lowercase.
    providedservice = models.CharField(db_column='ProvidedService', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spa_service'
        unique_together = (('serviceid', 'providedservice'),)


class StoreImage(models.Model):
    branchid = models.OneToOneField(Block, models.DO_NOTHING, db_column='BranchID', primary_key=True)  # Field name made lowercase.
    blockid = models.ForeignKey(Block, models.DO_NOTHING, db_column='BlockID', to_field='BlockID')  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'store_image'
        unique_together = (('branchid', 'blockid', 'image'),)


class Supplier(models.Model):
    supplierid = models.CharField(db_column='SupplierID', primary_key=True, max_length=8)  # Field name made lowercase.
    suppliername = models.CharField(db_column='SupplierName', max_length=50)  # Field name made lowercase.
    mail = models.CharField(db_column='Mail', max_length=45)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supplier'


class Supplies(models.Model):
    branchid = models.OneToOneField(Room, models.DO_NOTHING, db_column='BranchID', primary_key=True)  # Field name made lowercase.
    sppid = models.ForeignKey('SupplyType', models.DO_NOTHING, db_column='SppID')  # Field name made lowercase.
    supplyindex = models.PositiveIntegerField(db_column='SupplyIndex')  # Field name made lowercase.
    condition = models.CharField(db_column='Condition', max_length=45, blank=True, null=True)  # Field name made lowercase.
    roomnumber = models.ForeignKey(Room, models.DO_NOTHING, db_column='RoomNumber', to_field='RoomNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supplies'
        unique_together = (('branchid', 'supplyindex', 'sppid'),)


class SupplyType(models.Model):
    sppid = models.CharField(db_column='SppID', primary_key=True, max_length=6)  # Field name made lowercase.
    sppname = models.CharField(db_column='SppName', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supply_type'


class Supplying(models.Model):
    sppid = models.OneToOneField(SupplyType, models.DO_NOTHING, db_column='SppID', primary_key=True)  # Field name made lowercase.
    branchid = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchID')  # Field name made lowercase.
    supplierid = models.ForeignKey(Supplier, models.DO_NOTHING, db_column='SupplierID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supplying'
        unique_together = (('sppid', 'branchid'),)


class Zone(models.Model):
    branchid = models.OneToOneField(Branch, models.DO_NOTHING, db_column='BranchID', primary_key=True)  # Field name made lowercase.
    zonename = models.CharField(db_column='ZoneName', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zone'
        unique_together = (('branchid', 'zonename'),)
