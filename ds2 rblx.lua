local DataStore2 = require(1936396537)

local MainKey = "HelloWorld"
DataStore2.Combine( MainKey, "Money", "Furniture")

local function CreateDataTable()
	local PlayerData = {
		Money = {
			["Money"] = 10;
		};
		Furniture = {
			["PC"] = false;
		};
	}
	return PlayerData
end

game.Players.PlayerAdded:Connect(function(plr)
	local PlayerData = DataStore2(MainKey, plr):Get(CreateDataTable())
	
	local LS = Instance.new("Folder")
	LS.Name = "leaderstats"
	
	local Furniture = Instance.new("Folder")
	Furniture.Name = "Furniture"
	
	local Money = Instance.new("IntValue")
	Money.Name = "Money"
	
	local PC = Instance.new("BoolValue")
	PC.Name = "PC"
	
	local MoneyData = DataStore2("Money", plr)
	local FurnitureData = DataStore2("Furniture", plr)
	
	local function UpdateMoney(UpdatedStats)
		Money.Value = DataStore2(MainKey, plr):Get(UpdatedStats)["Money"]["Money"]
	end
	
	local function updateFurniture(UpdatedStats)
		PC.Value = DataStore2(MainKey, plr):Get(UpdatedStats)["Furniture"]["PC"]
		print(DataStore2(MainKey, plr):Get(UpdatedStats)["Furniture"]["PC"])
	end
	
	UpdateMoney(PlayerData)
	updateFurniture(PlayerData)
	DataStore2(MainKey, plr):OnUpdate(UpdateMoney)
	DataStore2(MainKey, plr):OnUpdate(updateFurniture)
	
	LS.Parent = plr
	Furniture.Parent = plr
	Money.Parent = LS
	PC.Parent = Furniture
	
	PC.Changed:Connect(function()
		local Furniture = FurnitureData:Get()
		Furniture.PC = true
		FurnitureData:Set(Furniture)
	end)
end)
