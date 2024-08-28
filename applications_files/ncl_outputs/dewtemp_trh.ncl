; ncl -n dewtemp_trh.ncl >> dewtemp_trh_output.txt

do tk=273,374
	do rh=1,100
		begin
		print(dewtemp_trh(tk,rh)-273.15)
		end
	end do
end do
