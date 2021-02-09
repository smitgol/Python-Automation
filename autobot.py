from selenium import webdriver
from time import sleep 
from selenium.webdriver.common.keys import Keys


## for blocking notification
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

## getting location of webdriver
path = input("Enter Webdriver Full path ")
driver = webdriver.Chrome(path, chrome_options=chrome_options)
driver.maximize_window()



driver.get('https://www.facebook.com/')
sleep(1)

username = input("Enter Email id or mobile no ")
password = input("Enter Password ")

email_field = driver.find_element_by_id('email')
email_field.send_keys(username)
sleep(1)

password_field = driver.find_element_by_id('pass')
password_field.send_keys(paswword)

login_but = driver.find_element_by_id('u_0_b')
login_but.click()

### account update task

dropdown_button = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]')
dropdown_button.click()

sleep(3)

see_profile = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[1]/a/div[1]')
see_profile.click()


sleep(4)

edit_profile = driver.find_element_by_css_selector('#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.dp1hu0rb.cbu4d94t.j83agx80 > div > div > div.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0 > div.rq0escxv.d2edcug0.ecyo15nh.hv4rvrfc.dati1w0a.tr9rh885 > div > div.rq0escxv.l9j0dhe7.du4w35lb.d2edcug0.hpfvmrgz.o387gat7.buofh1pr.g5gj957u.aov4n071.oi9244e8.bi6gxh9e.h676nmdw.aghb5jc5.rek2kq2y > div.lpgh02oy > div > div:nth-child(1) > div > div > div > div > div.sej5wr8e > div:nth-child(1) > div > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.taijpn5t.bp9cbjyn.owycx6da.btwxx1t3.c4xchbtz.by2jbhx6 > div > span > span')
edit_profile.click()

sleep(3)

update_information = driver.find_element_by_css_selector('#mount_0_0 > div > div:nth-child(1) > div > div:nth-child(7) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div.k3cnv2bo.t2oxmq98.cbu4d94t.j83agx80 > div.ofv0k9yr.b3onmgus.ph5uu5jm.ecm0bbzt.pygxslno > div > div:nth-child(1) > div > a > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.taijpn5t.bp9cbjyn.owycx6da.btwxx1t3.c4xchbtz.by2jbhx6 > div > span > span')
update_information.click()

sleep(3)

update_per_info = driver.find_element_by_css_selector('#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.dp1hu0rb.cbu4d94t.j83agx80 > div > div > div.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0 > div > div > div > div:nth-child(1) > div > div > div > div > div.ls2amcm3.pcp91wgn.ihqw7lf3.p8fzw8mz.discj3wi.pfnyh3mw.rq0escxv.maa8sdkg > div:nth-child(7) > a > span')
update_per_info.click()

sleep(3)

update_about_me = driver.find_element_by_css_selector('#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.dp1hu0rb.cbu4d94t.j83agx80 > div > div > div.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0 > div > div > div > div:nth-child(1) > div > div > div > div > div.buofh1pr > div > div > div:nth-child(1) > div.oygrvhab > div > a > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.g5gj957u.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr.o8rfisnq.p8fzw8mz.pcp91wgn.iuny7tx3.ipjc6fyt > span')
update_about_me.click()

sleep(2)

about_me = input("Enter about me")
enter_detail = driver.find_element_by_tag_name('textarea')
enter_detail.send_keys("testing")

save_button = driver.find_element_by_css_selector('#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.dp1hu0rb.cbu4d94t.j83agx80 > div > div > div.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0 > div > div > div > div:nth-child(1) > div > div > div > div > div.buofh1pr > div > div > div:nth-child(1) > div.oygrvhab > div > div.pybr56ya.i1fnvgqd.j83agx80.l6v480f0 > div.f9o22wc5.j83agx80 > div.oajrlxb2.s1i5eluu.gcieejh5.bn081pho.humdl8nn.izx4hr6d.rq0escxv.nhd2j8a9.j83agx80.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.d1544ag0.qt6c0cv9.tw6a2znq.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.l9j0dhe7.abiwlrkh.p8dawk7l.beltcj47.p86d2i9g.aot14ch1.kzx2olss.cbu4d94t.taijpn5t.ni8dbmo4.stjgntxs.k4urcfbm.tv7at329')
save_button.click()

sleep(2)

friend_list = driver.find_element_by_css_selector('#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.dp1hu0rb.cbu4d94t.j83agx80 > div > div > div.rq0escxv.lpgh02oy.du4w35lb.rek2kq2y > div > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.g5gj957u.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.i1fnvgqd.gs1a9yip.owycx6da.btwxx1t3.pxsmfnpt.pedkr2u6.n1dktuyu.dvqrsczn.l23jz15m.d4752i1f > div > div > div > div > div > div > a:nth-child(4) > div.bp9cbjyn.rq0escxv.j83agx80.pfnyh3mw.frgo5egb.l9j0dhe7.cb02d2ww.hv4rvrfc.dati1w0a > span')
friend_list.click()

sleep(1)

friends_profile = driver.find_element_by_css_selector('#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.dp1hu0rb.cbu4d94t.j83agx80 > div > div > div.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0 > div > div > div > div:nth-child(1) > div > div > div > div > div.j83agx80.btwxx1t3.lhclo0ds.i1fnvgqd > div:nth-child(1) > div.buofh1pr.hv4rvrfc > div:nth-child(1) > a')
friends_profile.click()

sleep(1)

comment = input("Enter comment to post ")
friends_comment = driver.find_element_by_css_selector('#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.dp1hu0rb.cbu4d94t.j83agx80 > div > div > div.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0 > div.rq0escxv.d2edcug0.ecyo15nh.hv4rvrfc.dati1w0a.tr9rh885 > div > div.rq0escxv.l9j0dhe7.du4w35lb.d2edcug0.hpfvmrgz.gile2uim.buofh1pr.g5gj957u.aov4n071.oi9244e8.bi6gxh9e.h676nmdw.aghb5jc5 > div:nth-child(3) > div:nth-child(1) > div > div > div > div > div > div > div > div > div > div > div:nth-child(2) > div > div:nth-child(4) > div > div > div.cwj9ozl2.tvmbv18p > div.ecm0bbzt.hv4rvrfc.e5nlhep0.dati1w0a.j83agx80.btwxx1t3.lzcic4wl > div.g3eujd1d.ni8dbmo4.stjgntxs.rz4wbd8a > div._25-w > div > div > div > form > div > div > div._5rpb > div > div > div > div')
friends_comment.send_keys("testing")
friends_comment.send_keys(Keys.ENTER)

driver.back()
driver.back()

sleep(1)

places_lived = driver.find_element_by_css_selector('#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.dp1hu0rb.cbu4d94t.j83agx80 > div > div > div.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0 > div > div > div > div:nth-child(1) > div > div > div > div > div.ls2amcm3.pcp91wgn.ihqw7lf3.p8fzw8mz.discj3wi.pfnyh3mw.rq0escxv.maa8sdkg > div:nth-child(4) > a > span')
places_lived.click()

sleep(2)

city_name = driver.find_element_by_css_selector('#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.dp1hu0rb.cbu4d94t.j83agx80 > div > div > div.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0 > div > div > div > div:nth-child(1) > div > div > div > div > div.buofh1pr > div > div > div > div.oygrvhab > div > div > div.buofh1pr > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.g5gj957u.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr.o8rfisnq.p8fzw8mz.pcp91wgn.iuny7tx3.ipjc6fyt > div.ii04i59q.a3bd9o3v.jq4qci2q.oo9gr5id.tvmbv18p > a > div > span')

targeted_city = city_name.text

print(targeted_city)

sleep(1)
search_people = driver.find_element_by_css_selector('#mount_0_0 > div > div:nth-child(1) > div > div:nth-child(4) > div.rq0escxv.byvelhso.q10oee1b.poy2od1o.j9ispegn.kr520xx4.ooia0uwo.kavbgo14.ekbqdzos > div > div > div > div > label > input')
search_people.send_keys(targeted_city)
search_people.send_keys(Keys.ENTER)

sleep(2)

peoples_but = driver.find_element_by_css_selector('#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.jifvfom9.gs1a9yip.owycx6da.btwxx1t3.buofh1pr.dp1hu0rb.ka73uehy > div.rq0escxv.l9j0dhe7.tkr6xdv7.j83agx80.cbu4d94t.pfnyh3mw.d2edcug0.hpfvmrgz.dp1hu0rb.rek2kq2y.o36gj0jk > div > div.q5bimw55.rpm2j7zs.k7i0oixp.gvuykj2m.j83agx80.cbu4d94t.ni8dbmo4.eg9m0zos.l9j0dhe7.du4w35lb.ofs802cu.pohlnb88.dkue75c7.mb9wzai9.d8ncny3e.buofh1pr.g5gj957u.tgvbjcpo.l56l04vs.r57mb794.kh7kg01d.c3g1iek1.k4xni2cv > div.j83agx80.cbu4d94t.buofh1pr.l9j0dhe7 > div.aov4n071 > div > div > div:nth-child(2) > div:nth-child(3) > a > div.ow4ym5g4.auili1gw.rq0escxv.j83agx80.buofh1pr.g5gj957u.i1fnvgqd.oygrvhab.cxmmr5t8.hcukyx3x.kvgmc6g5.nnctdnn4.hpfvmrgz.qt6c0cv9.jb3vyjys.l9j0dhe7.du4w35lb.bp9cbjyn.btwxx1t3.dflh9lhu.scb9dxdr > div.ow4ym5g4.auili1gw.rq0escxv.j83agx80.buofh1pr.g5gj957u.i1fnvgqd.oygrvhab.cxmmr5t8.hcukyx3x.kvgmc6g5.tgvbjcpo.hpfvmrgz.qt6c0cv9.rz4wbd8a.a8nywdso.jb3vyjys.du4w35lb.bp9cbjyn.btwxx1t3.l9j0dhe7 > div > div > div > div > span > span')
peoples_but.click()

sleep(2)

send_request = driver.find_element_by_css_selector('#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.jifvfom9.gs1a9yip.owycx6da.btwxx1t3.buofh1pr.dp1hu0rb.ka73uehy > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.g5gj957u.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr.dp1hu0rb > div > div > div > div > div > div > div:nth-child(1) > div > div > div > div > div > div > div.ozuftl9m.taijpn5t.cbu4d94t.j83agx80 > span > div')
send_request.click()

print("Done")
input("press anything to quit")
driver.quit()
