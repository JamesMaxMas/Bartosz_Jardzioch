-----------------------------------------------------------------------------------------
--
-- main.lua
--
-----------------------------------------------------------------------------------------

-- Your code here
local number_size = 70



local tlo = display.newImageRect( "obrazy/tlo.png", 360, 570 )
tlo.x = display.contentCenterX
tlo.y = display.contentCenterY

local pier = display.newImageRect( "obrazy/pier.png", 100, 120 )
pier.x = display.contentCenterX - 105
pier.y = 10

local pier1 = display.newImageRect( "obrazy/pier1.png", 100, 120 )
pier1.x = display.contentCenterX -10
pier1.y = 10

local pier2 = display.newImageRect( "obrazy/pier1.png", 100, 120 )
pier2.x = display.contentCenterX + 90
pier2.y = 10

local pier11 = display.newImageRect( "obrazy/pier.png", 100, 120 )
pier11.x = display.contentCenterX + 10
pier11.y = 100

local pier12 = display.newImageRect( "obrazy/pier1.png", 100, 120 )
pier12.x = display.contentCenterX + 90
pier12.y = 100

local tapCount = 0

local tapText = display.newText( tapCount, display.contentCenterX, 15,native.systemFont, number_size )
tapText:setFillColor( 0, 0, 0 )

local tapCount1 = 1

local tapText1 = display.newText( tapCount1, display.contentCenterX -100, 105,native.systemFont, number_size )
tapText1:setFillColor( 0, 0, 0 )

local tapCount2 = 0

local tapText2 = display.newText( tapCount2, display.contentCenterX + 80, 105,native.systemFont, number_size )
tapText2:setFillColor( 0, 0, 0 )

function funkcja(x)
  return function(event)
    tapCount = tapCount * 10
    tapCount = tapCount + x
    tapText.text = tapCount

  end
end
function back_f()
  
    tapCount = tapCount / 10
    tapCount = math.floor(tapCount)
    tapText.text = tapCount
  
end
function clear()
    tapCount = 0
    tapText.text = tapCount
end
function oblicz()
    
    tapCount1 = 1
    tapCount2 = tapCount
    
    
    
    if tapText1 == nil then 
    tapText1 = display.newText( tapCount1, display.contentCenterX -100, 105,native.systemFont, number_size )
    tapText1:setFillColor( 0, 0, 0 )
    tapText1.text = tapCount1
    end
    
    if tapText2 == nil then 
    
    
    pier2 = display.newImageRect( "obrazy/pier1.png", 100, 120 )
    pier2.x = display.contentCenterX + 90
    pier2.y = 10

    pier11 = display.newImageRect( "obrazy/pier.png", 100, 120 )
    pier11.x = display.contentCenterX + 10
    pier11.y = 100

    pier12 = display.newImageRect( "obrazy/pier1.png", 100, 120 )
    pier12.x = display.contentCenterX + 90
    pier12.y = 100
    
    tapText2 = display.newText( tapCount2, display.contentCenterX + 80, 105,native.systemFont, number_size )
    tapText2:setFillColor( 0, 0, 0 )
    end
    
    tapText2.text = tapCount2
    local num = {}
    local square = {}
    for x = 100, 2, -1 do
        table.insert(num,x)
        table.insert(square,x*x)
    end
    
    for i,x in ipairs(square) do
        
        if math.floor(tapCount2 / x) == (tapCount2 / x) then
            tapCount1 = tapCount1 *num[i]
            tapText1.text = tapCount1
            tapCount2 = tapText.text / x
            tapText2.text = tapCount2
        end 
    end
    if tapCount == 1 then
        pier2:removeSelf()
        pier2 = nil
        pier11:removeSelf()
        pier11 = nil
        pier12:removeSelf()
        pier12 = nil 
        tapText2:removeSelf()
        tapText2 = nil
    
    elseif tapCount2 ==  1 and pier11 ~= nil and pier12 ~= nil and tapText2 ~= nil then
        print("USUWAM")
        pier11:removeSelf()
        pier11 = nil
        pier12:removeSelf()
        pier12 = nil 
        tapText2:removeSelf()
        tapText2 = nil
    
    elseif tapCount1 ==  1 and tapText1 ~= nil then
        print("USUWAM")
       tapText1:removeSelf()
       tapText1 = nil
       print(tapText1)
    end
end



local a1 = display.newImageRect( "obrazy/a1.jpg", number_size, number_size )
a1.x = display.contentCenterX - number_size
a1.y = display.contentCenterY - number_size
a1.value = 1
a1:addEventListener( "tap", funkcja(a1.value))
local a2 = display.newImageRect( "obrazy/a2.jpg", number_size, number_size )
a2.x = display.contentCenterX
a2.y = display.contentCenterY - number_size
a2.value = 2
a2:addEventListener( "tap", funkcja(a2.value))


local a3 = display.newImageRect( "obrazy/a3.jpg", number_size, number_size )
a3.x = display.contentCenterX + number_size
a3.y = display.contentCenterY - number_size
a3.value = 3
a3:addEventListener( "tap", funkcja(a3.value))
local a4 = display.newImageRect( "obrazy/a4.jpg", number_size, number_size )
a4.x = display.contentCenterX - number_size
a4.y = display.contentCenterY
a4.value = 4
a4:addEventListener( "tap", funkcja(a4.value))
local a5 = display.newImageRect( "obrazy/a5.jpg", number_size, number_size )
a5.x = display.contentCenterX
a5.y = display.contentCenterY
a5.value = 5
a5:addEventListener( "tap", funkcja(a5.value))
local a6 = display.newImageRect( "obrazy/a6.jpg", number_size, number_size )
a6.x = display.contentCenterX + number_size
a6.y = display.contentCenterY
a6.value = 6
a6:addEventListener( "tap", funkcja(a6.value))
local a7 = display.newImageRect( "obrazy/a7.jpg", number_size, number_size )
a7.x = display.contentCenterX - number_size
a7.y = display.contentCenterY + number_size
a7.value = 7
a7:addEventListener( "tap", funkcja(a7.value))
local a8 = display.newImageRect( "obrazy/a8.jpg", number_size, number_size )
a8.x = display.contentCenterX
a8.y = display.contentCenterY + number_size
a8.value = 8
a8:addEventListener( "tap", funkcja(a8.value))
local a9 = display.newImageRect( "obrazy/a9.jpg", number_size, number_size )
a9.x = display.contentCenterX + number_size
a9.y = display.contentCenterY + number_size
a9.value = 9
a9:addEventListener( "tap", funkcja(a9.value))
local a0 = display.newImageRect( "obrazy/a0.jpg", number_size, number_size )
a0.x = display.contentCenterX
a0.y = display.contentCenterY + 2* number_size
a0.value = 0
a0:addEventListener( "tap", funkcja(a0.value))
local back = display.newImageRect( "obrazy/back.png", number_size, number_size )
back.x = display.contentCenterX + number_size
back.y = display.contentCenterY + 2* number_size
back:addEventListener( "tap", back_f)

local clear_b = display.newText( "C", display.contentCenterX - number_size, display.contentCenterY + 2* number_size , native.systemFont, number_size)
clear_b:setFillColor( 0, 0, 0 )
clear_b.x = display.contentCenterX - number_size
clear_b.y = display.contentCenterY + 2* number_size
clear_b:addEventListener( "tap", clear)

local oblicz_b = display.newImageRect( "obrazy/oblicz.png", 200, number_size )
oblicz_b.x = display.contentCenterX 
oblicz_b.y = display.contentCenterY *2 - 20
oblicz_b:addEventListener( "tap", oblicz)

