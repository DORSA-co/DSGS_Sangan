<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="20008000">
	<Property Name="varPersistentID:{0BBE4CA3-DDEC-4E77-860C-E800D4BCB95F}" Type="Ref">/My Computer/User Lib.lvlib/Is Admin?</Property>
	<Property Name="varPersistentID:{0F75DDAE-F089-4EBE-8CFD-6D4D650FABB7}" Type="Ref">/My Computer/User Lib.lvlib/Username</Property>
	<Property Name="varPersistentID:{2B15D217-358B-46A6-A6E6-0E35E0F6C689}" Type="Ref">/My Computer/Parameters Lib.lvlib/Thresholds</Property>
	<Property Name="varPersistentID:{2C3A872F-490B-4A2C-B2CC-E94984B127A6}" Type="Ref">/My Computer/User Lib.lvlib/Cancel Login</Property>
	<Property Name="varPersistentID:{3E58E472-D20F-4561-8CF1-AF543BA1154B}" Type="Ref">/My Computer/Setting Lib.lvlib/Abort</Property>
	<Property Name="varPersistentID:{536DE245-7672-48CB-9933-7F77CEE03257}" Type="Ref">/My Computer/Parameters Lib.lvlib/Area Threshold</Property>
	<Property Name="varPersistentID:{66AD492A-1215-4AF0-A663-5C154902D7C7}" Type="Ref">/My Computer/Parameters Lib.lvlib/Width Threshold</Property>
	<Property Name="varPersistentID:{AC120EB5-8F38-494B-B726-24601AD48975}" Type="Ref">/My Computer/Parameters Lib.lvlib/Reject Based on</Property>
	<Property Name="varPersistentID:{CE25F19D-1F64-4F51-869E-C8DEAFF0300E}" Type="Ref">/My Computer/User Lib.lvlib/User Flag</Property>
	<Property Name="varPersistentID:{F1B7A254-E391-4191-B5F0-166319272985}" Type="Ref">/My Computer/Parameters Lib.lvlib/Length Threshold</Property>
	<Property Name="varPersistentID:{F3C00829-B243-4A3F-A107-C856953793F4}" Type="Ref">/My Computer/User Lib.lvlib/Is Dorsa?</Property>
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="Database Lib.lvlib" Type="Library" URL="../Database Lib.lvlib"/>
		<Item Name="Main.vi" Type="VI" URL="../Main.vi"/>
		<Item Name="Maintenance Lib.lvlib" Type="Library" URL="../Maintenance Lib.lvlib"/>
		<Item Name="Parameters Lib.lvlib" Type="Library" URL="../Parameters Lib.lvlib"/>
		<Item Name="Setting Lib.lvlib" Type="Library" URL="../Setting Lib.lvlib"/>
		<Item Name="User Lib.lvlib" Type="Library" URL="../User Lib.lvlib"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Check if File or Folder Exists.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Check if File or Folder Exists.vi"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="GOOP Object Repository Method.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/_goopsup.llb/GOOP Object Repository Method.ctl"/>
				<Item Name="GOOP Object Repository Statistics.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/_goopsup.llb/GOOP Object Repository Statistics.ctl"/>
				<Item Name="GOOP Object Repository.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/_goopsup.llb/GOOP Object Repository.vi"/>
				<Item Name="Image Type" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/Image Type"/>
				<Item Name="IMAQ Create" Type="VI" URL="/&lt;vilib&gt;/vision/Basics.llb/IMAQ Create"/>
				<Item Name="IMAQ Image.ctl" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/IMAQ Image.ctl"/>
				<Item Name="IMAQ ReadFile 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ ReadFile 2"/>
				<Item Name="IMAQ Write BMP File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write BMP File 2"/>
				<Item Name="IMAQ Write File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write File 2"/>
				<Item Name="IMAQ Write Image And Vision Info File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write Image And Vision Info File 2"/>
				<Item Name="IMAQ Write JPEG File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write JPEG File 2"/>
				<Item Name="IMAQ Write JPEG2000 File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write JPEG2000 File 2"/>
				<Item Name="IMAQ Write PNG File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write PNG File 2"/>
				<Item Name="IMAQ Write TIFF File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write TIFF File 2"/>
				<Item Name="LVRowAndColumnTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVRowAndColumnTypeDef.ctl"/>
				<Item Name="NI_Database_API.lvlib" Type="Library" URL="/&lt;vilib&gt;/addons/database/NI_Database_API.lvlib"/>
				<Item Name="NI_FileType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/lvfile.llb/NI_FileType.lvlib"/>
				<Item Name="NI_MABase.lvlib" Type="Library" URL="/&lt;vilib&gt;/measure/NI_MABase.lvlib"/>
				<Item Name="NI_MAPro.lvlib" Type="Library" URL="/&lt;vilib&gt;/measure/NI_MAPro.lvlib"/>
				<Item Name="NI_PackedLibraryUtility.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/LVLibp/NI_PackedLibraryUtility.lvlib"/>
				<Item Name="Space Constant.vi" Type="VI" URL="/&lt;vilib&gt;/dlg_ctls.llb/Space Constant.vi"/>
				<Item Name="System Exec.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/system.llb/System Exec.vi"/>
				<Item Name="VariantType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/VariantDataType/VariantType.lvlib"/>
			</Item>
			<Item Name="lvanlys.dll" Type="Document" URL="/&lt;resource&gt;/lvanlys.dll"/>
			<Item Name="nivision.dll" Type="Document" URL="nivision.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="nivissvc.dll" Type="Document" URL="nivissvc.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
