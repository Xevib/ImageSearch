class ImgSearch(object):
    def __init__(self):
        pass

    def search(self,filename,out):
        from mechanize import Browser,HTMLForm
        import cookielib
        
        cj = cookielib.LWPCookieJar()
        br = Browser()
        br.set_cookiejar(cj)
        br.set_handle_robots(False)
        
        br.set_handle_equiv(True)
        br.set_handle_gzip(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.addheaders = [('user-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36')]
        page = br.open('https://www.google.es/imghp?sbi=1')
        
        form = HTMLForm('https://www.google.es/searchbyimage/upload', method="POST",enctype="multipart/form-data")
        form.new_control('file', 'encoded_image', {'id':"qbfile"})
        form.fixup()
        form.find_control("encoded_image").readonly = False
        
        form.set_all_readonly(False)
        form.add_file(open(filename), 'text/plain', filename)
        br.form=form
        response=br.submit()
        
        data=response.read()
        f=open(out,"w")
        f.write(data)
        f.close()
        
         
