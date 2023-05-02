Create database nikiatestdb;
CREATE TABLE groceries (
    Items varchar(50),
    Price int
);
INSERT INTO `nikiatestdb`.`groceries` (`Items`, `Price`) VALUES ('Apples', '5');
INSERT INTO `nikiatestdb`.`groceries` (`Items`, `Price`) VALUES ('Celery', '2');
INSERT INTO `nikiatestdb`.`groceries` (`Items`, `Price`) VALUES ('Orange', '4');
INSERT INTO `nikiatestdb`.`groceries` (`Items`, `Price`) VALUES ('Banana', '1');

select * from groceries;