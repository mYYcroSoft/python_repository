povolena_ip = "123.456.789.0"  # Tvoje povolená IP adresa

# Funkce pro ověření IP adresy
def overit_ip(adresa):
    if adresa == povolena_ip:
        return True
    else:
        return False

# Zakódování serverového kódu
zakodovany_kod = '''
   ESX = exports["es_extended"]:getSharedObject()



Citizen.CreateThread(function()
    while true do
        Citizen.Wait(900000)
        if Config.autopay == true then  
            TriggerEvent('vel_invoice:autopay')
        end
    end
end)


RegisterNetEvent('vel_invoice:create_invoice', function(invoice_data)
    xPlayer_creator = ESX.GetPlayerFromId(invoice_data.player_id.creator)
    xPlayer_target = ESX.GetPlayerFromId(invoice_data.player_id.target)
    identifiers = {creator = xPlayer_creator.getIdentifier(), target = xPlayer_target.getIdentifier()}
 
    MySQL.Async.execute('INSERT INTO vel_invoice (invoice_id, price,creator, target, company_creator, create_date, pay_date, title,reason) VALUES (@invoice_id, @price,@creator, @target, @company_creator, @create_date, @pay_date, @title, @reason)',
    {
        ['invoice_id'] = invoice_data.invoice_id,
        ['price'] = invoice_data.price,
        ['creator'] = identifiers.creator,
        ['target'] = identifiers.target,
        ['company_creator'] = invoice_data.company,
        ['create_date'] = invoice_data.date_data.create_date,
        ['pay_date'] = invoice_data.date_data.pay_date,
        ['title'] = invoice_data.reason.title,
        ['reason'] = invoice_data.reason.reason,
    },
    function(rowsChanged)
       print("[NEW INVOICE]" .. invoice_data.invoice_id)
    end)

end)

RegisterNetEvent('vel_invoice:getTraget_invoice')
AddEventHandler('vel_invoice:getTraget_invoice', function(id)
    xPlayer_target = ESX.GetPlayerFromId(id)
    local target_identifier = xPlayer_target.getIdentifier()
    local target_job = xPlayer_target.getJob().name
    MySQL.Async.fetchAll('SELECT * FROM vel_invoice WHERE target = @target', {['@target'] = target_identifier}, function(result)
        TriggerClientEvent('vel_invoice:receiveTarget_invoice', id, result)
    end)

    MySQL.Async.fetchAll('SELECT * FROM vel_invoice WHERE company_creator = @target_job', {['@target_job'] = target_job}, function(result)
        
        TriggerClientEvent('vel_invoice:receiveCompany_invoice', id, result)
    end)

end)


RegisterNetEvent('vel_invoice:payinvoice', function(playerid, invoiceid)
    xPlayer = ESX.GetPlayerFromId(playerid)
    identifier = xPlayer.getIdentifier()

    MySQL.Async.fetchAll('SELECT * FROM vel_invoice WHERE target = @target', {['@target'] = identifier}, function(result)
        for _, invoice in ipairs(result) do 
            if invoice.invoice_id == invoiceid then 
                playerPayinvoice(identifier,invoice.company_creator, invoice.price, invoice.invoice_id)
            end
        end
    end)
end)


function playerPayinvoice(identifier, company, price, invoice_id)
    local playerLoad = ESX.GetPlayerFromIdentifier(identifier)
   
    print("PLAYER:" .. playerLoad.getName() .. " | Pay Invoice:" .. invoice_id .. " - " .. price .. "$ | Player Bank:" .. playerLoad.getMoney())
    playerLoad.removeMoney(price)
 
	TriggerEvent('esx_addonaccount:getSharedAccount', 'society_' .. company, function(account)
	        if account then
                account.addMoney(price)
                removePlayerinvoice(invoice_id)
            
            else
                print("Company does't exist")
            end

	end)
end

function removePlayerinvoice(invoice_id)
    print("Invoice" .. invoice_id .. " > REMOVED!")
    MySQL.Async.execute(
        'DELETE FROM vel_invoice WHERE invoice_id = @invoiceId',
        {['@invoiceId'] = invoice_id})
end

RegisterNetEvent('vel_invoice:remove', function(id)

    removePlayerinvoice(id)
end)

RegisterNetEvent('vel_invoice:autopay', function()
    local date = os.date("%m/%d/%Y")
    print("AUTO PAY - " .. date) 
        MySQL.Async.fetchAll('SELECT * FROM vel_invoice WHERE pay_date = @pay_date', {['@pay_date'] = date}, function(result)
            for _, invoice in ipairs(result) do 
               targetXplayer = ESX.GetPlayerFromIdentifier(invoice.target)
               playerPayinvoice(invoice.target, invoice.company_creator, invoice.price, invoice.invoice_id)
            end
            
        end)
end)

RegisterServerEvent('getPlayerName')
AddEventHandler('getPlayerName', function(playerId)
    local player = ESX.GetPlayerFromId(playerId)
    if player then
        local playerName = player.getName()

        TriggerClientEvent('receivePlayerName', -1, playerId, playerName)
    end
end)


RegisterNetEvent('getPlayerNameByIdentifier', function(player_id, dat_x)

xPlayer_target = ESX.GetPlayerFromIdentifier(dat_x.target)
player_name = xPlayer_target.getName()
TriggerClientEvent('vel_invoice:receiveCompany_invoice_sendNUI', player_id, dat_x, player_name)
end)

'''

# Funkce pro spuštění serverového kódu
def spustit_kod():
    adresa_klienta = input("Zadej IP adresu klienta: ")
    if overit_ip(adresa_klienta):
        exec(zakodovany_kod)  # Spuštění zakódovaného kódu
    else:
        print("Tato IP adresa není povolena.")

# Zde můžeš spustit funkci pro spuštění serverového kódu
spustit_kod()
