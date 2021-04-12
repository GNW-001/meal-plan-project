
/* These are the tables created for the Meal Plan database*/
Use MealPlanDB;
/*--------------------------------------------------Tables Related to the User--------------------------------------------------*/
create table Activity_lvl(
    Activity_Type varchar(20),
    Calorie_Intake int,
    Calorie_Out int,

    
    primary key(Activity_Type)
    );

create table User(
    UID varchar(15),
    FName varchar(15),
    LName varchar(15),
    Email varchar(15),
    Password varchar(15),
    Height varchar(15),
    Weight varchar(15),
    Activity_Type varchar(15),
    
    primary key(UID),

    foreign key(Activity_Type) references Activity_lvl(Activity_Type) on delete cascade on update cascade
    );



/*-------------------------------------Tables Related to Allergy Information-------------------------------------*/
create table Allergy(
    ALID varchar(16),
    name varchar(30),

    primary key(ALID)
    );

create table Allergen(
    AID varchar(16),
    name varchar(30),
    
    primary key(AID)
    );

create table Affected_By(
    UID varchar(15),
    ALID varchar(16),
    
    primary key(UID,ALID),

    foreign key(UID) references User(UID) on delete cascade on update cascade,
    foreign key(ALID) references Allergy(ALID) on delete cascade on update cascade
);

create table Caused_By(
    ALID varchar(16),
    AID varchar(15),
    
    primary key(ALID, AID),

    foreign key(ALID) references Allergy(ALID) on delete cascade on update cascade,
    foreign key(AID) references Allergen(AID) on delete cascade on update cascade
);

create table Ingredients(
    IID varchar(15),
    Ingredients varchar(30),
    Calories int,
    
    primary key(IID)
);

create table Allergen_Is(
    AID varchar(15),
    IID varchar(15),
    
    primary key(AID, IID),

    foreign key(AID) references Allergen(AID) on delete cascade on update cascade,
    foreign key(IID) references Ingredients(IID) on delete cascade on update cascade
);

/*-------------------------------------Tables Related to Diseases & Deficiencies------------------------------------*/

create table Disease(
    DisID varchar(16),
    name varchar(40),
    
    primary key(DisID)
    );

create table Deficiency(
    DefID varchar(16),
    name varchar(40),
    
    primary key(DefID)
    );

create table Afflicted_with(
    UID varchar(15),
    DisID varchar(6),
    
    primary key(UID, DisID),

    foreign key(UID) references User(UID) on delete cascade on update cascade,
    foreign key(DisID) references Disease(DisID) on delete cascade on update cascade
);

create table Prone_To(
    UID varchar(5),
    DefID varchar(6),
    
    primary key(UID, DefID),

    foreign key(UID) references User(UID) on delete cascade on update cascade,
    foreign key(DefID) references Deficiency(DefID) on delete cascade on update cascade
);

/*-------------------------------------Tables Related to Meal Plan------------------------------------*/

create table MealPreference(
    PrefID varchar(5),
    name varchar(30),

    primary key(PrefID)
);

create table User_Prefers(
    UID varchar(5),
    PrefID varchar(5),
    
    primary key(UID, PrefID),

    foreign key(UID) references User(UID) on delete cascade on update cascade,
    foreign key(PrefID) references MealPreference(PrefID) on delete cascade on update cascade
);

create table MealPlan(
    MPID varchar(6),
    MDate date,

    primary key(MPID,Mdate)
);

create table MealType(
    MTID varchar(6),
    Mtype varchar(10),

    primary key(MTID)
);

create table Meal(
    MID varchar(5),
    Name varchar(40),
    img varchar(250),
    Calories int,
    MTID varchar(6),

    primary key(MID),
    
    foreign key(MTID) references MealType(MTID) on delete cascade on update cascade

);



create table Plan_Contains(
    MPID varchar(6),
    MID varchar(5),
    Day varchar(10),
    
    primary key(MPID,MID,Day),

    foreign key(MPID) references MealPlan(MPID) on delete cascade on update cascade,
    foreign key(MID) references Meal(MID) on delete cascade on update cascade
);

create table Recieves_Plan(
    UID varchar(5),
    MPID varchar(6),
    
    primary key(UID, MPID),

    foreign key(UID) references User(UID) on delete cascade on update cascade,
    foreign key(MPID) references MealPlan(MPID) on delete cascade on update cascade,
);
/*-------------------------------------Tables Related to Recipe------------------------------------*/

Create table RecipeType(
    RTID varchar(6),
    Rtype varchar(10),

    primary key(RTID)
);

Create table Recipe(
    RID varchar(5),
    RTID varchar(6),
    name varchar(40),

    primary key(RID)
);

Create table RecipeInstructions(
    RIID varchar(6),
    StepNumber int,
    step varchar(200),

    primary key(RIID)
);

Create table Measurements(
    MesID varchar(6),
    Size varchar(6),
    Amount decimal(10,2),
    
    primary key(MesID)
);

Create table Recipe_Incorporates(
    RID varchar(5),
    IID varchar(5),
    MesId varchar(6),

    primary key(RID,IID,MesID),

    foreign key(RID) references Recipe(RID) on delete cascade on update cascade,
    foreign key(IID) references Ingredients(IID) on delete cascade on update cascade,
    foreign key(MesID) references Measurements(MesID) on delete cascade on update cascade
);

Create table Comprise_Of(
    RID varchar(5),
    RIID varchar(6),

    primary key(RID, RIID),

    foreign key(RID) references Recipe(RID) on delete cascade on update cascade,
    foreign key(RIID) references RecipeInstructions(RIID) on delete cascade on update cascade
);

Create table Meal_Includes(
    MID varchar(5),
    RID varchar(6),

    primary key(MID,RID),

    foreign key(MID) references Meal(MID) on delete cascade on update cascade,
    foreign key(RID) references Recipe(RID) on delete cascade on update cascade
);

Create table Create_Recipe(
    UID varchar(5),
    RID varchar(6),
    Rdate date,

    primary key(UID, RID),

    foreign key(UID) references User(UID) on delete cascade on update cascade,
    foreign key(RID) references Recipe(RID) on delete cascade on update cascade
);


/*-------------------------------------Tables Related to Stock------------------------------------*/

create table Stock_Includes(
    STID varchar(6),
    IID varchar(5),
    MesID varchar(6),

    primary key(STID),
    
    foreign key(IID) references Ingredients(IID) on delete cascade on update cascade,
    foreign key(MesID) references Measurements(MesID) on delete cascade on update cascade
);

create table Stock(
    StockID varchar(6),
    STID varchar(6),

    primary key(StockID),
    foreign key(STID) references Stock_Includes(STID) on delete cascade on update cascade
);

create table Has_Stock(
    UID varchar(5),
    StockID varchar(6),

    primary key(UID, StockID),
    
    foreign key(UID) references User(UID) on delete cascade on update cascade,
    foreign key(StockID) references Stock(StockID) on delete cascade on update cascade
);


DELIMITER //
CREATE PROCEDURE getShoppingList(in MealPID varchar(6), useerid varchar(5))
BEGIN
    Select Ingredients.name, Measurements.size, Sum(Measurements.amount)from Recipe_Incorporates 
    Inner Join Meal_Includes on Meal_Includes.RID=Recipe_Incorporates.RID
    Inner Join Plan_Contains on Plan_Contains.MID=Meal_Includes.MID
    Inner Join Ingredients on Ingredients.IID=Recipe_Incorporates.IID
    Inner Join Measurements on Measurements.MesID=Recipe_Incorporates.MesID
    Inner Join Recieves_Plan on Recieves_Plan.MPID= Plan_Contains.MPID
    where Plan_Contains.MPID=MealPID
    group by Recipe_Incorporates.iid;

END //
    
DELIMITER ;
