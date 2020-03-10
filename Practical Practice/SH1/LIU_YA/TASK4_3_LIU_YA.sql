SELECT Device.SerialNumber, Device.Model, Device.Location, Monitor.DateCleaned
FROM Device, Monitor 
WHERE Device.Type="Monitor"  
GROUP BY Device.SerialNumber 
